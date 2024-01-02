-- Day 6: Wait for It

import Data.List
main :: IO()
main = do
 input <- getContents
 let races :: [String] = lines input

 let times :: [Integer] = [read x :: Integer | x <- tail . words $ head races]
 let distances :: [Integer] = [read x :: Integer | x <- tail . words $ last races]

 putStrLn . show $ solve_1 times distances


 let time :: Integer = read (concat . tail . words $ head races) :: Integer
 let distance :: Integer = read (concat . tail . words $ last races) :: Integer

 putStrLn . show $ solve_2 time distance


discriminant :: Integer -> Integer -> Float
discriminant t d = sqrt (fromIntegral (t * t - 4 * d))

quadratic :: Integer -> Integer -> (Float, Float)
quadratic t d = ((fromIntegral t + discriminant t d) * 0.5, (fromIntegral t - discriminant t d) * 0.5)

wins_per_race :: (Integer, Integer) -> Integer
wins_per_race race = (ceiling (fst r) - 1) - (floor (snd r) + 1) + 1
 where
 t :: Integer = fst race
 d :: Integer = snd race
 r :: (Float, Float) = quadratic t d


solve_1 :: [Integer] -> [Integer] -> Integer
solve_1 times distances = product $ map wins_per_race $ zip times distances

--Not solved, there are some precision issues with such a large number.
solve_2 :: Integer -> Integer -> Integer
solve_2 t d = wins_per_race (t, d)
