import Foundation

func getGenerateNumber(of num: Int) -> Int {
    var ret = num
    let num = String(num)
    num.forEach { ret += Int(numericCast($0.unicodeScalars.first!.value) - 48) } // 0은 아스키코드로 48
    return ret
}

func main() {
    let n = Int(readLine()!)!
    var result = [Int]()
    for i in 1...n {
        if getGenerateNumber(of: i) == n {
            result.append(i)
        }
    }
    print(result.isEmpty ? 0 : result.min()!)
}

main()
