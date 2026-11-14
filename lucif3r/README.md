
```zsh
python -m venv .venv
source .venv/bin/activate
```

```zsh
python -m venv venv
source ~/android-build-venv/bin/activate
```

```zsh
pyside6-android-deploy \
--name test01 \
--wheel-pyside=/home/kali/pyside-setup/dist_android/pyside6-6.12.0-6.12.0-cp310-abi3-android_aarch64.whl \
--wheel-shiboken=/home/kali/pyside-setup/dist_android/shiboken6-6.12.0-6.12.0-cp310-abi3-android_aarch64.whl \
--sdk-path=/home/kali/Android/Sdk \
--ndk-path=/home/kali/Android/Sdk/ndk/28.2.13676358
```
