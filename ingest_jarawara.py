import sys
from elanfile import ElanFile
import pprint

# def get_vernacular_glosses(d):
#     liste = list(d.values())[0]
#     vernacular = [el[0] for el in liste]
#     gloss  = [el[1] for el in liste]
#     return vernacular, gloss
#
# def cldf(v,g,t):
#     vernacular_cell="\t".join(v)
#     gloss_cell="\t".join(g)
#     translation_cell=t
#     return(f'"{vernacular_cell}","{gloss_cell}","{translation_cell}"')


if __name__ == '__main__':
    filename = sys.argv[1]
    eaf = ElanFile(filename, "http://no.url")
    eaf.populate_transcriptions()
    eaf.populate_translations()
    # pprint.pprint(eaf.translations)
    eaf.populate_glosses()
    eaf.populate_comments(['phrase-item'], comment_tier_id_to_retain='A_phrase-note-en')
    # print(eaf.transcriptions_with_IDs)
    print(eaf.comments)
    # tmp = eaf.glossed_sentences['morph-item']['A_morph-gls-en']
    # eaf.glossed_sentences = {'morph-item': {'A_morph-gls-en':tmp}}
    cldf_content = eaf.get_cldfs()
    # print(cldf_content)
    filename_cldf = filename.replace(".eaf",".csv")
    with open(filename_cldf,"w") as cldf_out:
        cldf_out.write(cldf_content)





