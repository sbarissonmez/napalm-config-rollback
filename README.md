### Napalm Config Rollback

Loading a configuration onto a device blindly, without verifying which lines actually change, can be a dangerous game, especially if the configuration that is being loaded has hundreds of lines or was generated programmatically. So, wouldn't it be nice if we could get a visual representation of all the changes that will be applied to our configuration and then decide whether we actually want to go ahead and apply them or discard the changes?

This is exactly what NAPALM allows you to do by using the `compare_config()` function together with `commit_config()` and `rollback()`.
