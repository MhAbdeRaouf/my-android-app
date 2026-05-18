[app]
title = MyApp
package.name = myapp
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# cython==0.29.33 مثبت من الـ workflow — لا تضعه هنا
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# arch واحدة فقط في البداية — أسرع وأقل مشاكل
android.archs = arm64-v8a

android.allow_backup = True
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1