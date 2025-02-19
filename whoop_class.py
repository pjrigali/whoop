from whoop import WhoopClient
from dataclasses import dataclass
from universal import USERNAME, PASSWORD, START_DATE, END_DATE, SPORT_DCT


def flatten_dict(d: dict, parent_key: str = '', sep: str = '_') -> dict:
    """
    Flatten a nested dictionary.

    Parameters:
    - d: The dictionary to flatten.
    - parent_key: The prefix key.
    - sep: The separator between parent and child keys.

    Returns:
    - A flattened dictionary.
    """
    l = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            l.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            l.append((new_key, v))
    return dict(l)


@dataclass
class Whoop:
    
    def __init__(self) -> None:
        self.client = WhoopClient(username=USERNAME, password=PASSWORD)
        self.profile = self.client.get_profile()


    def list_cycles(self, start_dt: str = None, end_dt: str = None, flat: bool = False, clean: bool = True) -> list:
        if not start_dt:
            start_dt = START_DATE
            
        if not end_dt:
            end_dt = END_DATE
        
        lst = self.client.get_cycle_collection(start_date=start_dt, end_date=end_dt)
        
        if flat:
            lst = [flatten_dict(d=i, parent_key='', sep='_') for i in lst]
        
        if clean:
            for i in lst:
                i['whoop_type'] = 'cycle'
                
                for j in ('start', 'end'):
                    if j in i:
                        i[f"{j}_ts"] = i[j]
                        del i[j]
        
        return lst


    def list_recoveries(self, start_dt: str = None, end_dt: str = None, flat: bool = False, clean: bool = True) -> list:
        if not start_dt:
            start_dt = START_DATE
            
        if not end_dt:
            end_dt = END_DATE
        
        lst = self.client.get_recovery_collection(start_date=start_dt, end_date=end_dt)

        if flat:
            lst = [flatten_dict(d=i, parent_key='', sep='_') for i in lst]
        
        if clean:
            for i in lst:
                i['whoop_type'] = 'recovery'
                
                for j in ('start', 'end'):
                    if j in i:
                        i[f"{j}_ts"] = i[j]
                        del i[j]
        
        return lst


    def list_sleeps(self, start_dt: str = None, end_dt: str = None, flat: bool = False, clean: bool = True) -> list:
        if not start_dt:
            start_dt = START_DATE
            
        if not end_dt:
            end_dt = END_DATE
        
        lst = self.client.get_sleep_collection(start_date=start_dt, end_date=end_dt)
        
        if flat:
            lst = [flatten_dict(d=i, parent_key='', sep='_') for i in lst]
        
        if clean:
            for i in lst:
                i['whoop_type'] = 'sleep'
            
                for j in ('start', 'end'):
                    if j in i:
                        i[f"{j}_ts"] = i[j]
                        del i[j]
                
        return lst


    def list_workouts(self, start_dt: str = None, end_dt: str = None, flat: bool = False, clean: bool = True) -> list:
        if not start_dt:
            start_dt = START_DATE
            
        if not end_dt:
            end_dt = END_DATE
        
        lst = self.client.get_workout_collection(start_date=start_dt, end_date=end_dt)
        
        if flat:
            lst = [flatten_dict(d=i, parent_key='', sep='_') for i in lst]
        
        if clean:
            for i in lst:
                i['whoop_type'] = 'workout'
                i['sport_name'] = SPORT_DCT.get(i['sport_id'])
            
                for j in ('start', 'end'):
                    if j in i:
                        i[f"{j}_ts"] = i[j]
                        del i[j]
        
        return lst
