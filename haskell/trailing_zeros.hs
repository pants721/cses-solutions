trailingZeros :: Int -> Int
trailingZeros n = sumTrailingZeros n 5
    where
        sumTrailingZeros num power
            | power > num = 0
            | otherwise   = (num `div` power) + sumTrailingZeros num (power * 5)

main :: IO()
main = print . trailingZeros . read =<< getLine
