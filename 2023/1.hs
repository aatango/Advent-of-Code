-- Day 1: Trebuchet?

-- Part One
import Data.Char

extract_digits :: String -> String
extract_digits s = filter isDigit s

decode_calibration :: String -> Integer
decode_calibration s = read [head $ extract_digits s, last $ extract_digits s] :: Integer

solve_1 :: [String] -> Integer
solve_1 ss = sum $ map decode_calibration ss


-- Part Two

-- Pre-process the input file beforehand, and then use it to solve part one.

{- Input File Pre-Processing
 - Replace the spelled number, with it's symbol;
 - beware, the spelling of two numbers might overlap (i.e., "eightwo" == 82)!
 - It is therefore not enough to simply search and replace a number at a time;
 - better search and replace with {SPELLING}{NUMBER}{SPELLING}:
 - for example, "eigh" == "eight8eight";
 - this allows any shared characters to still be present,
 - when replacing the next spelled number.
-}


main :: IO()
main = do
 input <- getContents
 let notes :: [String] = lines input

 putStrLn . show $ solve_1 notes
