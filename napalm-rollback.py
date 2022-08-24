from napalm import get_network_driver
driver = get_network_driver('eos')
device = driver('ip_address', 'username', 'password')
device.open()

device.load_replace_candidate(filename='device.conf')
print (device.compare_config())

if len(device.compare_config()) > 0:
    choice = input("\nWould you like to Replace the Configuration file? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        device.commit_config()

        choice = input("\nWould you like to Rollback to previous config? [yN]: ") 
        if choice == 'y':
            print('Rollback config is in progress ...')
            device.rollback()  
    else:
        print('Discarding ...')
        device.discard_config()
else:
    print ('No difference')

device.close()
print('Done.')