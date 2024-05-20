from objects.Symulation import Symulation
from objects.Repair_team.Config import Config

if __name__ == "__main__":
    config = Config(80, 1,True,100)
    Symulation().run(config)


#TODO uwzględnić koszta
#TODO uwzględnić koszty czy wzywamy w noc czy w dzień
