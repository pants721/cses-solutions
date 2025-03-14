bitStrings1 :: Int -> Integer
bitStrings1 n = 2^n `mod` ((10^9) + 7)

modulo = 10^9 + 7

modExp  :: Integer -> Integer -> Integer -> Integer
modExp base 0 modVal = 1
modExp base exp modVal
    | even exp  = halfExp * halfExp `mod` modVal
    | otherwise = base * modExp base (exp - 1) modVal `mod` modVal
    where
        halfExp = modExp base (exp `div` 2) modVal

bitStrings2 :: Int -> Integer
bitStrings2 n = modExp 2 (toInteger n) modulo

main :: IO()
main = print . bitStrings2 . read =<< getLine
