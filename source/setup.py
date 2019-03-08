import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "Turkey Trot!",
    options = {
                "build_exe": {
                    "packages": ["pygame"],
                    "include_files": [
                        "../resources/Backgrounds/Welcome.png",
                        "../resources/Backgrounds/LevelOneBackground.png",
                        "../resources/Backgrounds/LevelTwoBackground.png",
                        "../resources/Backgrounds/LevelThreeBackground.png",
                        "../resources/Backgrounds/map_screen.png",
                        '../resources/PlayerFrames/minWalk1.png',
                        '../resources/PlayerFrames/minWalk2.png',
                        '../resources/PlayerFrames/minWalk3.png',
                        '../resources/PlayerFrames/minWalk4.png',
                        '../resources/PlayerFrames/minWalk5.png',
                        '../resources/PlayerFrames/minWalk6.png',
                        "../resources/Berry/berrySmall.png",
                        "../resources/Pumpkin/pumpkin.png",
                        "../resources/Turkey/turkey.png",
                        "../resources/Berry/berry_big.png",
                        "../resources/Pumpkin/pumpkin_big.png",
                        "../resources/Turkey/turkey_big.png",
                        "../resources/Spider/spider.png",
                        '../resources/Heart/heart.png',
                        '../resources/Heart/heart_b.png',
                        "../resources/sound/background_music.ogg",
                        "../resources/sound/jump.wav",
                        "../resources/sound/Pickup_Coin.wav",
                        "../resources/sound/spiderSqueak.wav"
                        ]
                    }
                },
    executables = executables 
    )
        
        
