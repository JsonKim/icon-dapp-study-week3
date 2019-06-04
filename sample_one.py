from iconservice import *

TAG = 'SampleOne'

class InterfaceSample(InterfaceScore):
    @interface
    def getOwnerName(self):
        pass

class SampleOne(IconScoreBase):
    _OWNER_NAME = "owner_name"
    _ARRAY_DB_SAMPLE = "array_db_sample"
    _DICT_DB_SAMPLE = "dict_db_sample"

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._owner_name = VarDB(self._OWNER_NAME, db, str)
        self._dict_db = DictDB(self._DICT_DB_SAMPLE, db, str)

    def on_install(self) -> None:
        super().on_install()
        self._owner_name.set("Life4honor")

        self._dict_db["Jin"] = "Developer"
        self._array_db.put("Jin")

        self._dict_db["nanaones"] = "Developer"
        self._array_db.put("nanaones")

        self._dict_db["ICON"] = "Blockchain"
        self._array_db.put("ICON")

        self._dict_db["SCORE"] = "Smart Contract"
        self._array_db.put("SCORE")

    def on_update(self) -> None:
        super().on_update()
        self._owner_name.set("Life4honor v2")
 
    @property
    def _array_db(self):
        return ArrayDB(self._ARRAY_DB_SAMPLE, self.db, str)
   
    @external(readonly=True)
    def hello(self) -> str:
        owner = self._owner_name.get()
        elements = [(el, self._dict_db[el]) for el in self._array_db]
        return f"{owner} : Owner, {elements}"

    @payable
    def fallback(self):
        if self.msg.value >= 10000000000000000000:
            revert("ICX amout must be lower than 10")

    @payable
    @external
    def deposit(self):
        pass

    @external(readonly=True)
    def getOwnerName(self) -> str:
        return f'{self._owner_name.get()}, {self.msg.sender}'

    @external(readonly=True)
    def getOwnerNameInterface(self) -> str:
        interface = self.create_interface_score(self.address, InterfaceSample)
        return f'{interface.getOwnerName()}'

    @external(readonly=True)
    def getOwnerNameInnerFunc(self) -> str:
        return self.getOwnerName()

    @external(readonly=False)
    def setOwnerName(self, owner_name: str) -> str:
        self._owner_name.set(owner_name)
        self.OwnerNameChanged(owner_name)

    @eventlog
    def OwnerNameChanged(self, owner_name: str):
        pass
