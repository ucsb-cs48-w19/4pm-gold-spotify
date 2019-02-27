import unittest, argparse, pygame
from world import World
from player import Player


class world_test(unittest.TestCase):
    def setUp(self):
        self.world = World()
        self.world.mouse = [100, 200]
        self.click = [0]

    def test_init_world(self):
        self.assertEqual(self.world.state, 0)

    def test_start(self):
        self.world.start()
        self.assertGreater(len(self.world.ground), 0)

    def test_run_0(self):
        self.world.run()
        self.assertEqual(len(self.world.texts), 2)
        self.assertEqual(len(self.world.buttons), 1)

    def test_run_change_state(self):
        self.world.mouse = [400, 375]
        self.world.click = [1]
        self.world.run()
        self.assertEqual(self.world.state, 2)

    def test_user_input(self):
        self.assertEqual(self.world.player.x, 50)
        self.world.pressed_key = pygame.K_a
        self.world.user_input()
        self.assertEqual(self.world.player.x, 40)


class player_test(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, 200)

    def test_param_init(self):
        self.assertEqual(self.player.x, 100)
        self.assertEqual(self.player.y, 200)

    def test_move_left(self):
        self.player.move('left')
        self.assertEqual(self.player.x, 90)
        self.assertEqual(self.player.y, 200)
        self.assertEqual(self.player.state, 1)
        self.assertEqual(self.player.index, 1)

    def test_move_right(self):
        self.player.move('right')
        self.assertEqual(self.player.x, 110)
        self.assertEqual(self.player.y, 200)
        self.assertEqual(self.player.state, 1)
        self.assertEqual(self.player.index, 1)

    def test_hit_1(self):
        self.assertEqual(self.player.hit(), False)
        self.assertEqual(self.player.health, 80)
        self.assertGreater(self.player.immune_time, 0)

    def test_pick(self):
        self.assertEqual(self.player.pick(), 1)
        self.assertEqual(self.player.score, 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('test_code', type=str, nargs='?', default='all')
    args = parser.parse_args()
    test_code = args.test_code
    if test_code not in ["world", "player", "all"]:
        print("Please enter correct test code, include: world, player, all")
        exit(0)
    elif test_code == "world":
        suite = unittest.TestLoader().loadTestsFromTestCase(world_test)
    elif test_code == "player":
        suite = unittest.TestLoader().loadTestsFromTestCase(player_test)
    else:
        unittest.main(verbosity=2, argv=['first-arg-is-ignored'], exit=False)
        exit(0)
    # ignore the first arg because parser, verbosity set to 2 for more test info, change to 1 for less
    unittest.TextTestRunner(verbosity=2).run(suite)
    exit(0)

