import wget

# URL of the video
video_url = "https://scontent.cdninstagram.com/o1/v/t16/f1/m86/B94F3D52A0026B5F139F0FB2E974ADB5_video_dashinit.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLmNsaXBzLnVua25vd24tQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&vs=742778014509646_3096143156&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9COTRGM0Q1MkEwMDI2QjVGMTM5RjBGQjJFOTc0QURCNV92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dLRnd0eHJyZmk3QjE4RUJBUG1aUVRINzJRb0FicV9FQUFBRhUCAsgBACgAGAAbAYgHdXNlX29pbAExFQAAJv6bkYeb7L8%2FFQIoAkMzLBdASPCj1wo9cRgSZGFzaF9iYXNlbGluZV8xX3YxEQB1AAA%3D&ccb=9-4&oh=00_AYBp0Fk-F6oAEqrW-x-Q--DNt6EVnNvFgJw1H7QaFDPd8w&oe=66870D45&_nc_sid=1d576d"

# Download the video
video_filename = wget.download(video_url)

print(f"Video downloaded successfully: {video_filename}")
