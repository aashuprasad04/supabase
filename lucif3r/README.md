# Deploy Android App
1. Android Build Venv
   ```zsh
   python -m venv venv
   source ~/android-build-venv/bin/activate
   ```
2. Android app deploy
   ```zsh
   pyside6-android-deploy \
   --name test01 \
   --wheel-pyside=/home/kali/pyside-setup/dist_android/pyside6-6.12.0-6.12.0-cp310-abi3-android_aarch64.whl \
   --wheel-shiboken=/home/kali/pyside-setup/dist_android/shiboken6-6.12.0-6.12.0-cp310-abi3-android_aarch64.whl \
   --sdk-path=/home/kali/Android/Sdk \
   --ndk-path=/home/kali/Android/Sdk/ndk/28.2.13676358 \
   --keep-deployment-files
   ```
3. Update app 
   ```zsh
   buildozer android debug
   ```
4. Update app directly <inx>running abd command in linux machine</ins>
   ```zsh
   adb install -r test01-0.1-arm64-v8a-debug.apk
   ```
5. App Log using <ins>android</ins>
   ```zsh
   adb devices 
   ```
   ```zsh
   adb logcat -c
   ```
   ```zsh
   adb logcat -d -v time > ~/Desktop/app_error.txt
   ```
   ```zsh
   grep -iE "FATAL EXCEPTION|Traceback|Python|Qt|pyside|dlopen|AndroidRuntime|SIGABRT|libc" ~/Desktop/app_error.txt
   ```
   
