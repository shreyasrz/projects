import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


example_sent1 = '''In 1979 David Attenborough began to compose the body of work which would define his career. Life on Earth was to raise the standard of wildlife film making, and went on to influence the next generation of presenters. Meanwhile in the US, Marty Stouffer's Wild America programme was one of the most popular shows ever aired by PBS. First aired in 1981, the show was immediately successful and went on to be most broadcast series ever to have been shown on public television. Presenter Marty Stouffer played no small part in the popularity of the nature series and his likeable Arkansas bred boy next door personality made him a celebrity and a star. However, like Sir David Attenborough, Marty took a laid back approach, far different to that of a new celebrity who was about to make his mark on international wildlife programming with his larger than life style. Steve Irwin was an energetic Australian whose The Crocodile Hunter series debuted in Australia in 1996 before being snapped up by television channels all over the world. It was seen by audiences in over 130 countries, and Steve Irwin in his trademark khaki shorts with his catchphrase 'Crikey!' become one of the most accessible ambassadors for wildlife and conservation that the world had seen.
The storm before the dawn

Celebrity is a fickle beast and Marty Stouffer was fined for building a hunting camp on publicly owned lands in 1993 amid much publicity. His approach to wildlife was also coming under scrutiny and in the mid-90s was fined $362,000 dollars for hacking a trail through wilderness in Colorado to film migrating elk more closely. His contract with PBS was subsequently dropped and the last Wild America show was made in 1995. The untimely death of Steve Irwin in 2006 united audiences all over the world. Irwin was stabbed in the chest by a stingray barb while filming, and had previously been criticised for getting too close to animals in the wild. However, a new age of acceptance may have begun with the passing of Steve Irwin and over 300 million viewers around the world tuned in for his memorial service. Today his conservation work is carried on by his wide Terri and his Wildlife Warriors organisation and his daughter Bindi has presented her own series. Even Marty Stouffer has been vindicated to some extent. Many of the allegations against him were never proven, and Warner Brothers made a feature length film entitled Wild America based on his and his brother's lives in 1997. One celebrity who has remained above criticism is Sir David Attenborough. He continues to be a part of cutting edge wildlife and natural history documentaries that pave the way for a new, more aware type of presenter. His 2014 series Life Story which was shown in October 2014 was the first ever 4k programme to be made by the BBC, and new series of natural history documentaries are planned which are set to rival Planet Earth. He continues his successful collaboration with SKY and UKTV and Conquest of the Skies, a thrilling 3D feature will be shown at Christmas 2014. He may be in his 80s but in terms of celebrity, Sir David Attenborough's star has never been brighter. '''
example_sent2 = '''In 1979 David Attenborough began to compose the body of work which would define his career. Life on Earth was to raise the standard of wildlife film making, and went on to influence the next generation of presenters. Meanwhile in the US, Marty Stouffer's Wild America programme was one of the most popular shows ever aired by PBS. First aired in 1981, the show was immediately successful and went on to be most broadcast series ever to have been shown on public television. Presenter Marty Stouffer played no small part in the popularity of the nature series and his likeable Arkansas bred boy next door personality made him a celebrity and a star. However, like Sir David Attenborough, Marty took a laid back approach, far different to that of a new celebrity who was about to make his mark on international wildlife programming with his larger than life style. Steve Irwin was an energetic Australian whose The Crocodile Hunter series debuted in Australia in 1996 before being snapped up by television channels all over the world. It was seen by audiences in over 130 countries, and Steve Irwin in his trademark khaki shorts with his catchphrase 'Crikey!' become one of the most accessible ambassadors for wildlife and conservation that the world had seen.
The storm before the dawn

Celebrity is a fickle beast and Marty Stouffer was fined for building a hunting camp on publicly owned lands in 1993 amid much publicity. His approach to wildlife was also coming under scrutiny and in the mid-90s was fined $362,000 dollars for hacking a trail through wilderness in Colorado to film migrating elk more closely. His contract with PBS was subsequently dropped and the last Wild America show was made in 1995. The untimely death of Steve Irwin in 2006 united audiences all over the world. Irwin was stabbed in the chest by a stingray barb while filming, and had previously been criticised for getting too close to animals in the wild. However, a new age of acceptance may have begun with the passing of Steve Irwin and over 300 million viewers around the world tuned in for his memorial service. Today his conservation work is carried on by his wide Terri and his Wildlife Warriors organisation and his daughter Bindi '''
example_sent1=example_sent1.lower()
example_sent2=example_sent2.lower()
stop_words = set(stopwords.words("english"))
exclude = set(string.punctuation)
example_sent1 = ''.join(ch for ch in example_sent1 if ch not in exclude)
example_sent2 = ''.join(ch for ch in example_sent2 if ch not in exclude)

words1 = word_tokenize(example_sent1)
words2 = word_tokenize(example_sent2)

filt_sent1 = [w for w in words1 if not w in stop_words]
#print(filt_sent1)
filt_sent1 = sorted(set(filt_sent1))
print(filt_sent1)

filt_sent2 = [w for w in words2 if not w in stop_words]
#print(filt_sent2)
filt_sent2 = sorted(set(filt_sent2))
print(filt_sent2)

count=len(set(filt_sent1) & set(filt_sent2))
copied_content=count/len(filt_sent1)*100
print (copied_content,'%')