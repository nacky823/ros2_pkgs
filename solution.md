# エラーの対処録

colcon build 時に、

```
Starting >>> mypkg
Starting >>> person_msgs
/usr/lib/python3/dist-packages/setuptools/dist.py:723: UserWarning: Usage of dash-separated 'script-dir' will not be supported in future versions. Please use the underscore name 'script_dir' instead
  warnings.warn(
  /usr/lib/python3/dist-packages/setuptools/dist.py:723: UserWarning: Usage of dash-separated 'install-scripts' will not be supported in future versions. Please use the underscore name 'install_scripts' instead
    warnings.warn(
    Finished <<< person_msgs [0.58s]
    --- stderr: mypkg
    /usr/lib/python3/dist-packages/setuptools/dist.py:723: UserWarning: Usage of dash-separated 'script-dir' will not be supported in future versions. Please use the underscore name 'script_dir' instead
      warnings.warn(
      /usr/lib/python3/dist-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
        warnings.warn(
	---
	Finished <<< mypkg [0.66s]])
```

というエラーが出た。

```
udo apt install python3-pip
```
```
pip install setuptools==58.2.0
```

を実行すると、エラー文が変わった

```
/home/nacky/.local/lib/python3.10/site-packages/setuptools/dist.py:717: UserWarning: Usage of dash-separated 'script-dir' will not be supported in future versions. Please use the underscore name 'script_dir' instead
  warnings.warn(
  /home/nacky/.local/lib/python3.10/site-packages/setuptools/dist.py:717: UserWarning: Usage of dash-separated 'install-scripts' will not be supported in future versions. Please use the underscore name 'install_scripts' instead
    warnings.warn(
    Finished <<< person_msgs [0.62s]
    --- stderr: mypkg
    /home/nacky/.local/lib/python3.10/site-packages/setuptools/dist.py:717: UserWarning: Usage of dash-separated 'script-dir' will not be supported in future versions. Please use the underscore name 'script_dir' instead
      warnings.warn(
```

ros2_pkgs/mypkg/setup.cfg 内の scripts- -> scripts_ install-  -> install_ へ変えるとエラーは消えた
