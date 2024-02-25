def on_forever():
    scene.set_background_image(assets.image("""dino1"""))
    pause(900)
    scene.set_background_image(assets.image("""prof"""))
    pause(900)
forever(on_forever)
