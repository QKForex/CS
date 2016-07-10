
# parsetabhtml.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '67D196765C6411A86912751487B71A83'
    
_lr_action_items = {'$end':([0,1,2,3,5,6,7,10,17,24,],[-2,-5,-3,-14,0,-2,-4,-1,-8,-9,]),'STRING':([0,1,2,3,6,7,14,16,17,24,],[1,-5,-3,-14,1,-4,18,1,-8,-9,]),'WORD':([0,1,2,3,4,6,7,8,9,12,14,16,17,18,19,21,24,],[2,-5,-3,-14,8,2,-4,-6,11,11,19,2,-8,-13,-12,22,-9,]),'JAVASCRIPT':([0,1,2,3,6,7,16,17,24,],[3,-5,-3,-14,3,-4,3,-8,-9,]),'LANGLESLASH':([1,2,3,6,7,10,16,17,20,24,],[-5,-3,-14,-2,-4,-1,-2,-8,21,-9,]),'EQUAL':([0,1,2,3,6,7,11,16,17,24,],[7,-5,-3,-14,7,-4,14,7,-8,-9,]),'SLASHRANGLE':([8,9,12,13,15,18,19,],[-6,-11,-11,17,-10,-13,-12,]),'LANGLE':([0,1,2,3,6,7,16,17,24,],[4,-5,-3,-14,4,-4,4,-8,-9,]),'RANGLE':([8,9,12,13,15,18,19,22,23,],[-6,-11,-11,16,-10,-13,-12,-7,24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'tag_arguments':([9,12,],[13,15,]),'html':([0,6,16,],[5,10,20,]),'element':([0,6,16,],[6,6,6,]),'tagnameend':([21,],[23,]),'tag_argument':([9,12,],[12,12,]),'tagname':([4,],[9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> html","S'",1,None,None,None),
  ('html -> element html','html',2,'p_html','htmlgrammar.py',15),
  ('html -> <empty>','html',0,'p_html_empty','htmlgrammar.py',18),
  ('element -> WORD','element',1,'p_element_word','htmlgrammar.py',22),
  ('element -> EQUAL','element',1,'p_element_word_eq','htmlgrammar.py',26),
  ('element -> STRING','element',1,'p_element_word_string','htmlgrammar.py',30),
  ('tagname -> WORD','tagname',1,'p_tagname','htmlgrammar.py',34),
  ('tagnameend -> WORD','tagnameend',1,'p_tagnameend','htmlgrammar.py',40),
  ('element -> LANGLE tagname tag_arguments SLASHRANGLE','element',4,'p_element_tag_empty','htmlgrammar.py',49),
  ('element -> LANGLE tagname tag_arguments RANGLE html LANGLESLASH tagnameend RANGLE','element',8,'p_element_tag','htmlgrammar.py',56),
  ('tag_arguments -> tag_argument tag_arguments','tag_arguments',2,'p_tag_arguments','htmlgrammar.py',61),
  ('tag_arguments -> <empty>','tag_arguments',0,'p_tag_arguments_empty','htmlgrammar.py',65),
  ('tag_argument -> WORD EQUAL WORD','tag_argument',3,'p_tag_argument_word','htmlgrammar.py',69),
  ('tag_argument -> WORD EQUAL STRING','tag_argument',3,'p_tag_argument_string','htmlgrammar.py',73),
  ('element -> JAVASCRIPT','element',1,'p_element_javascript','htmlgrammar.py',77),
]
