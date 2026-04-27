#===================MyDB===================#
class NOT_SUCCESSFUL_CONNECT(Exception): pass
class MODIFICATION_IS_PROHIBITED(Exception): pass

class NOT_ACTIVE_DB(Exception): pass

class VOID_QUERY(Exception): pass

class BAD_SELECT_QUERY(Exception): pass
class BIG_SELECT_QUERY(Exception): pass

class BAD_INSERT_QUERY(Exception): pass
