import unittest, argparse
from world import World
from player import Player

class world_test(unittest.TestCase):
    def test_init_world(self):
        world = World()
        self.assertEqual(world.state, 0)

    def test_param_init(self):
        player = Player(100, 200)
        self.assertEqual(player.x, 100)
        self.assertEqual(player.y, 200)


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
        exit(1)
    # ignore the first arg because parser, verbosity set to 2 for more test info, change to 1 for less
    unittest.TextTestRunner(verbosity=2).run(suite)

