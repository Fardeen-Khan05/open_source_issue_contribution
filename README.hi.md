# 🐛 समस्या: आपके पहले ओपन सोर्स पीआर (PR) के लिए पाइथन गुड फर्स्ट इश्यूज (Python good first issues)

**शुरुआती लोगों के लिए अनुकूल पाइथन सीएलआई (CLI) जिसमें 30+ गुड फर्स्ट इश्यूज हैं।** इसमें जानबूझकर कुछ बग्स, गायब टेस्ट और छोटे फीचर्स छोड़े गए हैं जो आपके योगदान का इंतज़ार कर रहे हैं। इसे फोर्क करें, ठीक करें, एक पीआर (PR) खोलें और अपने गिटहब (GitHub) कॉन्ट्रिब्यूशन ग्राफ को हरा-भरा (green) बनाएं 🟩

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![good first issues](https://img.shields.io/badge/good%20first%20issues-30%2B-orange)

## 🎯 यह क्या है?

`fixit` एक छोटा कमांड लाइन टूलबॉक्स है (वर्ड काउंटर, यूनिट कन्वर्टर, पासवर्ड जेनरेटर, जेसन फॉर्मेटर, टेक्स्ट टूल्स)। यह **जानबूझकर अधूरा/दोषपूर्ण है**: कुछ टूल्स में बग हैं, कुछ टेस्ट गायब हैं और कुछ फीचर्स अभी नहीं बनाए गए हैं। हर समस्या एक खुला [इश्यू](../../issues) है जिसे आप चुन सकते हैं।

ओपन सोर्स में नए हैं? यह रिपॉजिटरी आपके लिए ही बनाई गई है। बड़े कोडबेस के साथ किसी पिछले अनुभव की आवश्यकता नहीं है।

## 🚀 5 मिनट में अपना पहला योगदान दें

1. [`good first issue`](../../labels/good%20first%20issue) लेबल वाले किसी **इश्यू को चुनें** और उस पर कमेंट करें कि `I'd like to work on this` (मैं इस पर काम करना चाहता हूँ)।

2. इस रिपॉजिटरी को **फोर्क (Fork)** करें (ऊपर दाएं कोने का बटन) और इसे क्लोन करें:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/open_source_issue_contribution.git
   cd open_source_issue_contribution
   ```

3. सेटअप करें:
   ```bash
   python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   pytest
   ```
4. एक नई ब्रांच बनाएं, समस्या को ठीक करें, और टेस्ट्स में से संबंधित `xfail` मार्कर को हटा दें:

   ```Bash
   git checkout -b fix-issue-12
   ```

5.टेस्ट चलाएं (`pytest`), कमिट करें, पुश करें और `Closes #12` का उल्लेख करते हुए एक Pull Request खोलें।

पूरी गाइड पढ़ें: `CONTRIBUTING.md`

## 🧰 टूल आज़माएं
   ```Bash
   fixit wc "hello world"
   fixit convert 100 c2f
   fixit password --length 16 --symbols
   fixit json '{"name":"fixit"}'
   fixit palindrome "Level"
   fixit reverse "open source is fun"
   ```
इनमें से कुछ कमांड्स आपको गलत आउटपुट देंगे। इस प्रोजेक्ट का उद्देश्य यही है! 😉

## 🗂 इश्यू लेबल्स (Issue labels)
| Label | Meaning |
|-------|-------|
| `good first issue` | आपके पहले PR के लिए बिल्कुल सही |
|`easy` / `medium` / `hard`	| कठिनाई का स्तर (Difficulty)|
|`bug`	| कोई टूल गलत परिणाम दे रहा है|
|`feature` |	एक नया कमांड या विकल्प|
|`tests` |	छूटे हुए टेस्ट्स लिखें|
|`documentation` |	डॉक्यूमेंटेशन या README में सुधार करें|

## 🤝 नियम (Rules)
प्रति PR केवल एक ही इश्यू पर काम करें, और काम शुरू करने से पहले उस इश्यू पर कमेंट ज़रूर करें।

केवल सार्थक योगदान (meaningful contributions) ही मर्ज किए जाएंगे। स्पैम या खाली PRs बंद कर दिए जाएंगे।

विनम्र रहें। Code of Conduct पढ़ें।

## 📄 लाइसेंस (License)
MIT। LICENSE देखें।

⭐ अगर इससे आपको मदद मिली हो, तो इस रिपॉजिटरी को स्टार (star) दें और अपने उन दोस्तों के साथ शेयर करें जो ओपन सोर्स शुरू करना चाहते हैं!
