from env.core.snake import Snake
from tests.validators.snake_validator import full_test_snake_step

TEST_HEAD_COORDINATES = (5, 5)
TEST_DIRECTION_INDEX = 1
TEST_SNAKE_LENGTH = 3


def main():
    if full_test_snake_step(TEST_HEAD_COORDINATES, TEST_DIRECTION_INDEX, TEST_SNAKE_LENGTH):

        print('\nLets try to use your step method:')

        test_snake = Snake((5, 5), 1, 3)
        print(f'\nYour Snake initial position: {test_snake.blocks}'
              f'\nAnd Snake direction: {test_snake.current_direction_index}')

        test_snake.step(1)
        print('\nPressing RIGHT button'
              f'\nNow your Snake position: {test_snake.blocks}'
              f'\nAnd Snake direction: {test_snake.current_direction_index}'
              '\nDirection didnt change as expected')

        test_snake.step(3)
        print('\nPressing LEFT button'
              f'\nNow your Snake position: {test_snake.blocks}'
              f'\nAnd Snake direction: {test_snake.current_direction_index}'
              '\nDirection didnt change as expected')

        test_snake.step(2)
        print('\nPressing DOWN button'
              f'\nNow your Snake position: {test_snake.blocks}'
              f'\nAnd Snake direction: {test_snake.current_direction_index}'
              '\nDirection changed as expected')

        test_snake.step(0)
        print('\nPressing UP button'
              f'\nNow your Snake position: {test_snake.blocks}'
              f'\nAnd Snake direction: {test_snake.current_direction_index}'
              '\nDirection didnt change as expected')

        print('\nAll actions were completed correctly'
              '\nWell done!')


if __name__ == "__main__":
    main()
