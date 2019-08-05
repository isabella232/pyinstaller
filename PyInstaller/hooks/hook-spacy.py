from PyInstaller.utils.hooks import collect_data_files
import spacy

# add datas for spacy
datas = collect_data_files('spacy', False)
datas += collect_data_files('spacy.data.en_core_web_lg', True)

# append spacies data path
datas.append((spacy.util.get_data_path(), 'spacy/data'))

hiddenimports=['cymem', 'cymem.cymem', 'thinc.linalg', 'murmurhash', 'murmurhash.mrmr', 'spacy.strings',
'spacy.morphology', 'spacy.lexeme', 'spacy.tokens', 'spacy.tokens.underscore', 'spacy.parts_of_speech',
'dill', 'spacy.tokens._retokenize', 'spacy.syntax', 'spacy.syntax.stateclass',
'spacy.syntax.transition_system', 'spacy.syntax.nonproj', 'spacy.syntax.nn_parser', 'spacy.syntax.arc_eager', 'thinc.extra.search',
'spacy.syntax._beam_utils', 'spacy.syntax.ner', 'thinc.neural._classes.difference', 'srsly.msgpack.util', 'preshed',
'preshed.maps', 'thinc.neural', 'thinc.neural._aligned_alloc', 'thinc', 'blis',
'blis.py', 'spacy.vocab', 'spacy.lemmatizer', 'spacy._align', 'spacy.util',
'spacy.lang', 'spacy.data.en', 'spacy.syntax._parser_model', 'spacy.matcher._schemas']