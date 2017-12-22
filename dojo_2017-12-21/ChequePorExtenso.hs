import Test.Hspec

main :: IO ()
main = hspec $ do
  describe "suite" $ do
    it " '1,00' tem que retornar 'um'" $ do
      extenso "1,00" `shouldBe` "um"
    it " '2,00' tem que retornar 'dois'" $ do
      extenso "2,00" `shouldBe` "dois"
    it "3" $ do
      extenso "3,00" `shouldBe` "tres"
    it "4" $ do
      shouldBe ( extenso "4,00" ) "quatro"
    it "5" $ do
      ( shouldBe $ extenso "5,00" ) "cinco"
    it "6" $ do
      extenso "6,00" `shouldBe` "seis"
    it "7" $ do
      extenso "7,00" `shouldBe` "sete"
    it "25" $ do
      extenso "25,00" `shouldBe` "vinte e cinco"
    it "23" $ do
      shouldBe ( extenso "23,00") "vinte e tres"
    it "28" $ do
      shouldBe ( extenso "28,00") "vinte e oito"
    it "29" $ do
      shouldBe ( extenso "29,00") "vinte e nove"
    it "32" $ do
      shouldBe ( extenso "32,00") "trinta e dois"
    it "33" $ do
      extenso "33,00" `shouldBe` "trinta e tres"
    it "333" $ do
      extenso "333,00" `shouldBe` "trezentos e trinta e tres"
    it "334" $ do
      extenso "334,00" `shouldBe` "trezentos e trinta e quatro"
    it "335" $ do
      extenso "335,00" `shouldBe` "trezentos e trinta e cinco"


------------------------------------------------
extenso :: String -> String
extenso "1,00" = "um"
extenso "2,00" = "dois"
extenso "3,00" = "tres"
extenso "4,00" = "quatro"
extenso "5,00" = "cinco"
extenso "6,00" = "seis"
-- extenso (x:xs) = if x == '6' then "seis" else extenso (x:xs)
extenso "7,00" = "sete"
extenso "8,00" = "oito"
extenso "9,00" = "nove"
extenso "334,00" = "trezentos e trinta e quatro"
extenso ('2':xs) = "vinte e " ++ extenso xs
extenso ('3':(x:(',':xs))) = "trinta e " ++ extenso (x:',':xs)
extenso _ = "trezentos e trinta e tres"

-- String = [Char]
-- 3,00 = ['3', ',', '0', '0']

--somar :: Int -> Int -> Int
--somar a b = a + b

-- map' ::  (a -> b) -> [a] -> [b]
-- map' _ [] = []
-- map' f (a:as) =  f a : map' f as
