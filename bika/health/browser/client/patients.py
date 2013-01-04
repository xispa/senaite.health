�
֬�Pc           @   s�  d  d l  m Z d  d l m Z d  d l m Z d  d l m Z d  d l m Z d  d l	 m
 Z
 m Z m Z d  d l m Z d  d l m Z d  d	 l m Z m Z d  d
 l m Z d  d l m Z d  d l m Z d  d l m Z d  d l Td  d l m Z m  Z  d  d l! m" Z" d  d l# m$ Z$ d  d l% m& Z& d  d l' m( Z( d  d l) m* Z* d  d l+ m, Z, d  d l- Z- d e f d �  �  YZ. d e f d �  �  YZ/ d e f d �  �  YZ0 d e0 f d �  �  YZ1 d e f d  �  �  YZ2 d! e f d" �  �  YZ3 d# e f d$ �  �  YZ4 d% e f d& �  �  YZ5 d' e f d( �  �  YZ6 d) e f d* �  �  YZ7 d+ e f d, �  �  YZ8 d- e f d. �  �  YZ9 d/ e f d0 �  �  YZ: d1 e f d2 �  �  YZ; d S(3   i����(   t   getSecurityManager(   t   DateTime(   t   REFERENCE_CATALOG(   t   getToolByName(   t   ViewPageTemplateFile(   t   PMFt   loggert   bikaMessageFactory(   t   BrowserView(   t   BatchFolderContentsView(   t   AnalysisRequestWorkflowActiont   AnalysisRequestsView(   t   BikaListingView(   t   Publish(   t   SamplesView(   t	   IContacts(   t   *(   t   doActionFort   skip(   t   isActive(   t
   itemgetter(   t   IFolderContentsView(   t	   IViewView(   t	   translate(   t
   implementsNt   ClientWorkflowActionc           B   s   e  Z d  Z d �  Z RS(   s}   This function is called to do the worflow actions
        that apply to objects transitioned directly from Client views

        The main lab 'analysisrequests' and 'samples' views also have
        workflow_action urls bound to this handler.

        The parent AnalysisRequestWorkflowAction handles
        AR and Sample context workflow actions (affecting parts/analyses)

    c         C   sW	  |  j  j } t j j | � t |  j d � } t |  j d � } t |  j t � } |  j j } |  j j	 j
 } d } | j | d � } | s� d } | j d d � } | s� |  j d k r� |  j  j d |  j j �  � |  _ n  |  j  j j |  j � d  Sn  | d k r�t j |  � }	 i g  d	 6g  d
 6}
 x�|	 j �  D]�\ } } | j d k re| } | j �  } n | } | j } | j | d d � d k r�q5n  | t | � s�q5n  d | k r5d | k r5y4 | d d | j �  } | d d | j �  } Wn t k
 rq5n X| r| pd } | r1t | � p4d } n q5| j | � | j | � | j �  | j �  } xO | D]G } | j �  | j  i d d 6� } x | D] } | j! �  j �  q�WqtW| r5| r5| j" | | � | j | d � } t" | | � |
 | j# | j$ �  � q5q5Wd  } x8|
 D]0} |
 | } t& | � d k r�| d	 k rxt' d d i d j( | � d 6�} n" t' d d i d j( | � d 6�} |  j j | � } |  j j) j* | d � q%t& | � d k r%| d	 k rt' d d i d j( | � d 6�} n" t' d d i d j( | � d 6�} |  j j | � } |  j j) j* | d � q%q%W| s�t' d � } |  j j | � } |  j j) j* | d � n  |  j  j d |  j j �  � |  _ |  j  j j |  j � n�| d k r�t j |  � }	 i  }
 g  } x�|	 j �  D]�\ } } | j d k r4| } | j �  } n | } | j } | j | d d � d k rdqn  | t+ | � syqn  d | k rd  | k ry4 | d d | j �  } | d  d | j �  } Wn t k
 r�qn X| r�| p�d } | r t | � pd } n qxL | j, d! � D]; } | j | d � d	 k r| j- | � | j. | � qqWxt | j, d! � D]c } | j | d � d	 k rk| r�| r�t" | | � | j$ �  |
 | j j$ �  <q�| j# | � qkqkWqWt& |
 j/ �  � d k rt' d" d i d j( |
 j/ �  � d 6�} n> t' d# d i d j( |
 j/ �  � d 6d j( |
 j0 �  � d$ 6�} |  j j | � } |  j j) j* | d � | r�| r�| r�t" | | � n  |  j  j d |  j j �  � |  _ |  j  j j |  j � nw| d+ k rF	t j |  � }	 g  } g  }
 xF |	 j �  D]8 \ } } t1 | � r| j2 t �  � | j# | � qqWt3 |  j |  j  | | � �  }
 t& |
 � d k r�t' d( d i d j( |
 � d 6�} nC t& |
 � d k r�t' d) d i d j( |
 � d 6�} n t' d* � } |  j j | � } |  j j) j* | d � |  j  j d |  j j �  � |  _ |  j  j j |  j � n t j4 |  � d  S(,   Nt   portal_workflowt   bika_catalogt   workflow_actiont    t   workflow_action_buttont   workflow_action_idt   referert   samplet   to_be_preservedt
   sample_duet   AnalysisRequestt   inactive_statet   inactivet
   getSamplert   getDateSampledi    t   to_be_sampledt   review_statei   s&   ${items} are waiting for preservation.t   mappings   , t   itemss$   ${items} are waiting to be received.t   infos$   ${item} is waiting for preservation.t   items"   ${item} is waiting to be received.s   No changes made.t   preservet   getPreservert   getDatePreservedt   SamplePartitions0   ${items}: partitions are waiting to be received.s+   ${item}: ${part} is waiting to be received.t   partt
   prepublisht   publisht	   republishs   ${items} were published.s   ${item} published.s   No items were published(   s
   prepublishs   publishs	   republish(5   t   requestt   formt   plonet   protectt   CheckAuthenticatorR   t   contextR   R   t   portal_membershipt   checkPermissiont   gett   destination_urlt
   get_headert   absolute_urlt   responset   redirectR
   t   _get_selected_itemsR,   t   portal_typet	   getSamplet	   aq_parentt
   getInfoFort   SampleSamplet   stript   KeyErrorR   t
   setSamplert   setDateSampledt   reindexObjectt   getAnalysisRequestst   getAnalysest	   getObjectR   t   appendt   Titlet   Nonet   lent   _t   joint   plone_utilst   addPortalMessaget   PreserveSamplet   objectValuest   setDatePreservedt   setPreservert   keyst   valuesR   t   setDatePublishedR   t   __call__(   t   selfR8   t   workflowt   bct   rcR   R>   t	   came_fromt   actiont   objectst   transitionedt   obj_uidt   objt   arR!   t   Samplert   DateSampledt   arst   analysest   at	   new_statet   messaget   statet   tt   not_transitionedt	   Preservert   DatePreservedt   spt   ARs_to_publish(    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyRb   %   s.   	


						"					(   t   __name__t
   __module__t   __doc__Rb   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR      s   
t   ClientBatchesViewc           B   s   e  Z d  �  Z d �  Z RS(   c         C   s3   t  t |  � j | | � |  j j �  d |  _ d  S(   Ns   /batches(   t   superR   t   __init__R<   RB   t   view_url(   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �   s    c         C   s�   t  |  j d � } g  |  j D] } | d |  j k r | ^ q d } i  } xW | d d d |  j j �  � D]7 } | j �  } | j �  rj | j �  | | j �  <qj qj W| j �  S(   NR   t   idi    RF   R$   t	   ClientUID(	   R   R<   t   review_statesR*   t   UIDRR   t   getBatchUIDt   getBatchR`   (   Rc   t   contentFilterRe   t   xRu   t   batchesRm   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyt   contentsMethod�   s    3(   R|   R}   R�   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR   �   s   	t   ClientAnalysisRequestsViewc           B   s   e  Z d  �  Z d �  Z RS(   c         C   s�   t  t |  � j | | � i d j | j �  � d 6d d 6|  j d <g  } x/ |  j D]$ } | d j d � | j | � qS W| |  _ d  S(   Nt   /t   queryi    t   levelt   patht   columnst   Client(	   R�   R�   R�   RX   t   getPhysicalPathR�   R�   t   removeRS   (   Rc   R<   R7   R�   R*   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �   s    c         C   s$  i  |  _  t |  j d � } t |  j d � } |  j j j } g  |  j j d � D]' } | j | d d � d k rO | ^ qO } t |  j � r|  j j d k r� | r� t	 d � } | |  j j
 | � � q| j t |  j � ri d	 d
 6d d 6|  j  |  j j
 t	 d � � <qn  t t |  � j �  S(   NR   R=   t   ContactR%   R   t   activeR�   s7   Client contact required before request may be submittedt   ar_addt   urls$   ++resource++bika.lims.images/add.pngt   icont   Add(   t   context_actionsR   R<   RY   RZ   R\   RI   R   RF   RW   R   R>   t   AddAnalysisRequestR�   R�   Rb   (   Rc   t   wft   mtoolRZ   t   ct   active_contactst   msg(    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyRb     s    	')(   R|   R}   R�   Rb   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �   s   	
t   ClientBatchAnalysisRequestsViewc           B   s   e  Z RS(    (   R|   R}   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�     s   t   ClientSamplesViewc           B   s   e  Z d  �  Z RS(   c         C   s�   t  t |  � j | | � i d j | j �  � d 6d d 6|  j d <g  } x/ |  j D]$ } | d j d � | j | � qS W| |  _ d  S(   NR�   R�   i    R�   R�   R�   R�   (	   R�   R�   R�   RX   R�   R�   R�   R�   RS   (   Rc   R<   R7   R�   R*   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�     s    (   R|   R}   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�     s   t   ClientARImportsViewc           B   s$   e  Z e e � d  �  Z d �  Z RS(   c         C   s�  t  t |  � j | | � d |  _ i d d 6d d 6|  _ i i d d 6d d	 6t d
 � 6|  _ t |  _ t |  _	 t
 |  _ d |  _ d |  _ |  j d |  _ t d � |  _ d |  _ i i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6|  _ i d d 6t d � d 6i  d 6d d d d d g d 6i d d 6t d  � d 6i d d! 6d 6d d d g d 6i d" d 6t d# � d 6i d" d! 6d 6d d d d g d 6g |  _ d  S($   Nt   portal_catalogt   ARImportRF   t   sortable_titlet   sort_ons   createObject?type_name=ARImportR�   s$   ++resource++bika.lims.images/add.pngR�   s	   AR Importi2   t	   arimportss.   /++resource++bika.lims.images/arimport_big.pngs   Analysis Request ImportsR   t   Importt   titles   Date Importedt   getDateImportedt   Validityt	   getStatuss   Date Submittedt   getDateAppliedt   Statet   state_titlet   defaultR�   t   AllR�   R�   t   importedt   ImportedR*   t	   submittedt   Applied(   R�   R�   R�   t   catalogR�   RW   R�   t   Falset   show_sort_columnt   show_select_rowt   Truet   show_select_columnt   pagesizet   form_idt
   portal_urlR�   R�   t   descriptionR�   R�   (   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   -  sT    	

						




c         C   su   t  j |  � } x_ t t | � � D]K } | | j d � sA q" n  d | | d | | d f | | d d <q" W| S(   NRl   s   <a href='%s'>%s</a>R�   R�   t   replace(   R   t   folderitemst   rangeRV   t   has_key(   Rc   R,   R�   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   ^  s     -(   R|   R}   R   R   R�   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   *  s   
	1t   ClientAnalysisProfilesViewc           B   s)   e  Z d  Z d �  Z d �  Z d �  Z RS(   s[   This is displayed in the Profiles client action,
       in the "Analysis Profiles" tab
    c         C   s�  t  t |  � j | | � d |  _ i d d 6d d 6i d j |  j j �  � d 6d d	 6d
 6|  _ t |  _	 t |  _
 t |  _ d |  _ d |  _ |  j d |  _ t d � |  _ d |  _ i i t d � d 6d d 6d 6i t d � d 6d d 6d 6i t d � d 6d 6|  _ i d d 6t d � d 6i d d 6d 6i d d 6g d 6d d d g d 6i d  d 6t d! � d 6i d  d 6d 6i d" d 6g d 6d d d g d 6i d# d 6t d$ � d 6i  d 6d d d g d 6g |  _ d  S(%   Nt   bika_setup_catalogt   AnalysisProfileRF   R�   R�   R�   R�   i    R�   R�   i2   t   analysisprofiless5   /++resource++bika.lims.images/analysisprofile_big.pngs   Analysis ProfilesR   RT   R�   t   indext   DescriptionR�   s   Profile Keyt   getProfileKeyR�   R�   t   ActiveR�   R%   R�   t
   deactivatet   transitionsR�   R&   t   Dormantt   activatet   allR�   (   R�   R�   R�   R�   RX   R<   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RW   R�   R�   R�   R�   (   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   m  sH    							


c         C   sd   t  |  j d � } | j } | t |  j � rQ i d d 6d d 6|  j t d � <n  t t |  � j �  S(   NR=   s&   createObject?type_name=AnalysisProfileR�   s$   ++resource++bika.lims.images/add.pngR�   R�   (	   R   R<   R>   t   AddAnalysisProfileR�   RW   R�   R�   Rb   (   Rc   R�   R>   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyRb   �  s    	
c         C   su   t  j |  � } x_ t t | � � D]K } | | j d � sA q" n  d | | d | | d f | | d d <q" W| S(   NRl   s   <a href='%s'>%s</a>R�   R�   R�   (   R   R�   R�   RV   R�   (   Rc   R,   R�   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  s     -(   R|   R}   R~   R�   Rb   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   h  s   	-		t   ClientARTemplatesViewc           B   s)   e  Z d  Z d �  Z d �  Z d �  Z RS(   sW   This is displayed in the Templates client action,
       in the "AR Templates" tab
    c         C   s�  t  t |  � j | | � d |  _ i d d 6d d 6i d j |  j j �  � d 6d d	 6d
 6|  _ t |  _	 t |  _
 t |  _ d |  _ d |  _ |  j d |  _ t d � |  _ d |  _ i i t d � d 6d d 6d 6i t d � d 6d d 6d 6|  _ i d d 6t d � d 6i d d 6d 6i d d 6g d 6d d g d 6i d d 6t d � d 6i d d 6d 6i d  d 6g d 6d d g d 6i d! d 6t d" � d 6i  d 6d d g d 6g |  _ d  S(#   NR�   t
   ARTemplateRF   R�   R�   R�   R�   i    R�   R�   i2   t   artemplatess0   /++resource++bika.lims.images/artemplate_big.pngs   AR TemplatesR   RT   R�   R�   R�   R�   R�   R�   R�   R�   R%   R�   R�   R�   R�   R&   R�   R�   R�   R�   (   R�   R�   R�   R�   RX   R<   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RW   R�   R�   R�   R�   (   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  sF    							


c         C   sd   t  |  j d � } | j } | t |  j � rQ i d d 6d d 6|  j t d � <n  t t |  � j �  S(   NR=   s!   createObject?type_name=ARTemplateR�   s$   ++resource++bika.lims.images/add.pngR�   R�   (	   R   R<   R>   t   AddARTemplateR�   RW   R�   R�   Rb   (   Rc   R�   R>   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyRb   �  s    	
c         C   s�   t  j |  � } x� t t | � � D]m } | | j d � sA q" n  | | d } | j �  | | d <d | | d | | d f | | d d <q" W| S(   NRl   R�   s   <a href='%s'>%s</a>R�   R�   (   R   R�   R�   RV   R�   RT   (   Rc   R,   R�   Rl   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  s     -(   R|   R}   R~   R�   Rb   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  s   	*		t   ClientSamplePointsViewc           B   s)   e  Z d  Z d �  Z d �  Z d �  Z RS(   s@   This is displayed in the "Sample Points" tab on each client
    c         C   s�  t  t |  � j | | � d |  _ i d d 6d d 6i d j |  j j �  � d 6d d	 6d
 6|  _ t |  _	 t |  _
 t |  _ d |  _ d |  _ |  j d |  _ t d � |  _ d |  _ i i t d � d 6d d 6d 6i t d � d 6d d 6d 6|  _ i d d 6t d � d 6i d d 6d 6i d d 6g d 6d d g d 6i d d 6t d � d 6i d d 6d 6i d  d 6g d 6d d g d 6i d! d 6t d" � d 6i  d 6d d g d 6g |  _ d  S(#   NR�   t   SamplePointRF   R�   R�   R�   R�   i    R�   R�   i2   t   SamplePointss1   /++resource++bika.lims.images/samplepoint_big.pngs   Sample PointsR   RT   R�   R�   R�   R�   R�   R�   R�   R�   R%   R�   R�   R�   R�   R&   R�   R�   R�   R�   (   R�   R�   R�   R�   RX   R<   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RW   R�   R�   R�   R�   (   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  sF    							


c         C   sd   t  |  j d � } | j } | t |  j � rQ i d d 6d d 6|  j t d � <n  t t |  � j �  S(   NR=   s"   createObject?type_name=SamplePointR�   s$   ++resource++bika.lims.images/add.pngR�   R�   (	   R   R<   R>   t   AddSamplePointR�   RW   R�   R�   Rb   (   Rc   R�   R>   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyRb     s    	
c         C   s�   t  j |  � } x� t t | � � D]m } | | j d � sA q" n  | | d } | j �  | | d <d | | d | | d f | | d d <q" W| S(   NRl   R�   s   <a href='%s'>%s</a>R�   R�   (   R   R�   R�   RV   R�   RT   (   Rc   R,   R�   Rl   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   &  s     -(   R|   R}   R~   R�   Rb   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  s   	*		t   ClientAnalysisSpecsViewc           B   s-   e  Z e e � d  �  Z d �  Z d �  Z RS(   c         C   s�  t  t |  � j | | � d |  _ i d d 6d d 6| j �  d 6i d j | j �  � d 6d	 d
 6d 6|  _ i  |  _ t	 |  _
 t	 |  _ t |  _ d |  _ d |  _ |  j d |  _ t d � |  _ i i t d � d 6d d 6d 6|  _ i d d 6t d � d 6i d d 6d 6i d d 6g d 6d g d 6i d d 6t d � d 6i d d 6d 6i d  d 6g d 6d g d 6i d! d 6t d" � d 6i  d 6d g d 6g |  _ d  S(#   NR�   t   AnalysisSpecRF   R�   R�   t   getClientUIDR�   R�   i    R�   R�   i2   t   analysisspecss2   /++resource++bika.lims.images/analysisspec_big.pngs   Analysis Specificationss   Sample TypeR�   t   getSampleTypeTitleR�   t
   SampleTypeR�   R�   R�   R�   R%   R�   R�   R�   R�   R&   R�   R�   R�   R�   (   R�   R�   R�   R�   R�   RX   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RW   R�   R�   R�   (   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   4  sD    							




c         C   s�   t  |  j d � } | j } t |  j � r� | t |  j � r` i d d 6d d 6|  j t d � <n  | t |  j � r� i d d 6d d 6|  j t d	 � <q� n  t t	 |  � j
 �  S(
   NR=   s#   createObject?type_name=AnalysisSpecR�   s$   ++resource++bika.lims.images/add.pngR�   R�   t   set_to_lab_defaultss-   ++resource++bika.lims.images/analysisspec.pngs   Set to lab defaults(   R   R<   R>   R   t   AddAnalysisSpecR�   RW   t   ManageClientsR�   R�   Rb   (   Rc   R�   R>   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyRb   `  s    	

c         C   s�   t  j |  � } x� t t | � � D] } | | j d � sA q" n  | | d } | j �  oj | j �  j �  | | d <d | | d | | d f | | d d <q" W| S(   NRl   R�   s   <a href='%s'>%s</a>R�   R�   (   R   R�   R�   RV   R�   t   getSampleTypeRT   (   Rc   R,   R�   Rl   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   n  s     -(   R|   R}   R   R   R�   Rb   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   1  s   
	,	t   SetSpecsToLabDefaultsc           B   s   e  Z d  Z d �  Z RS(   s>    Remove all client specs, and add copies of all lab specs
    c         C   sq  |  j  j } t |  j d � } | d d d |  j j �  � } | rk |  j j g  | D] } | j ^ qR � n  | d d d |  j j j j �  � } g  | D] } | j	 �  ^ q� } xb | D]Z } |  j j
 d d d d � } |  j | } | j �  | j d | j �  d	 | j �  � q� W|  j j }	 |  j j t d
 � � }
 |  j j j |
 d � |  j  j j |  j j �  d � d  S(   NR�   RF   R�   R�   t	   type_nameR�   t   tmpR�   t   ResultsRanges.   Analysis specifications reset to lab defaults.R-   s   /analysisspecs(   R7   R8   R   R<   R�   t   manage_delObjectsR�   t
   bika_setupt   bika_analysisspecsRR   t   invokeFactoryt   processFormt   editR�   t   getResultsRangeR   RW   RY   RZ   t   RESPONSERD   RB   (   Rc   R8   t   bsct   cst   st   lst   labspect   _idt
   clientspecR   Rt   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyRb   �  s.    )
		(   R|   R}   R~   Rb   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   }  s   t   ClientAttachmentsViewc           B   s-   e  Z e e � d  �  Z d �  Z d �  Z RS(   c         C   sM  t  t |  � j | | � i d d 6d d 6|  _ i  |  _ t |  _ t |  _ t |  _	 d |  _
 d |  _ |  j d |  _ t d � |  _ d	 |  _ i i t d
 � d 6d 6i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6|  _ i d d 6d d 6i  d 6d d d d d d g d 6g |  _ d  S(   Nt
   AttachmentRF   t   reverset
   sort_orderi2   t   attachmentss0   /++resource++bika.lims.images/attachment_big.pngt   AttachmentsR   s
   Request IDR�   t   getTextTitlet   Filet   AttachmentFiles   Attachment Typet   AttachmentTypes   Content Typet   ContentTypet   Sizet   FileSizes   Date Loadedt
   DateLoadedR�   R�   R�   R�   R�   (   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RW   R�   R�   R�   R�   (   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  s8    
							
c         C   s@   t  |  d � } | j | � } t | � r8 | d j �  S| Sd  S(   Nt   mimetypes_registryi    (   R   t   lookupRV   t   name(   Rc   R
  t   mimetoolt	   mimetypes(    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyt
   lookupMime�  s
    c         C   sX  t  j |  � } xBt t | � � D].} | | j d � sA q" n  | | d } | j �  } | j �  } | j �  } | j �  | | d <| j	 �  j
 �  | | d <| j	 �  j
 �  | | d <|  j | j �  � | | d <d | j �  d | | d <| j �  | | d <d	 | | | d
 f | | d d
 <d | | | d f | | d d <q" W| S(   NRl   R  R  R  s   %sKbi   R  R  s   <a href='%s'>%s</a>R   R�   s.   <a href='%s/at_download/AttachmentFile'>%s</a>(   R   R�   R�   RV   R�   RB   t   getAttachmentFilet   getBestIcont   filenamet   getAttachmentTypeRT   R  t   getContentTypet   get_sizet   getDateLoaded(   Rc   R,   R�   Rl   t   obj_urlt   fileR�   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  s&     !%(   R|   R}   R   R   R�   R  R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  s   
	#	t   ClientOrdersViewc           B   s$   e  Z e e � d  �  Z d �  Z RS(   c         C   s�  t  t |  � j | | � i d d 6d d 6d d 6|  _ i i d d 6d	 d
 6t d � 6|  _ t |  _ t |  _ t |  _	 t
 |  _ d |  _ d |  _ |  j d |  _ t d � |  _ i i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6|  _ i d d 6t d � d 6i  d 6d d d d g d 6i d d 6i d d 6d 6t d  � d 6d d g d 6i d! d 6i d! d 6d 6t d" � d 6d d d g d 6g |  _ d  S(#   Nt   SupplyOrderRF   R�   R�   R�   R�   s"   createObject?type_name=SupplyOrderR�   s$   ++resource++bika.lims.images/add.pngR�   R�   i   t   orderss+   /++resource++bika.lims.images/order_big.pngt   Orderss   Order NumberR�   t   OrderNumbers
   Order Datet	   OrderDates   Date Dispatchedt   DateDispatchedR�   R�   R�   R�   R�   R�   R�   t   pendingR*   t   Pendingt
   dispatchedt
   Dispatched(   R�   R  R�   R�   RW   R�   R�   t   show_table_onlyR�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   �  sL    

						




c         C   s�   t  j |  � } x� t t | � � D]� } | | j d � sA q" n  | | d } | j �  | | d <|  j | j �  � | | d <|  j | j �  � | | d <d | | d | | d f | | d d <q" W| S(   NRl   R  R  R  s   <a href='%s'>%s</a>R�   R�   (	   R   R�   R�   RV   R�   t   getOrderNumbert   ulocalized_timet   getOrderDatet   getDateDispatched(   Rc   R,   R�   Rl   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�     s     -(   R|   R}   R   R   R�   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR  �  s   
	-t   ClientContactsViewc           B   s'   e  Z e e e � d  �  Z d �  Z RS(   c         C   s#  t  t |  � j | | � d |  _ i d d 6d d 6i d j | j �  � d 6d d	 6d
 6|  _ i i d d 6d d 6t d � 6|  _ t	 |  _
 t	 |  _ t |  _ d |  _ d |  _ |  j d |  _ t d � |  _ d |  _ i i t d � d 6d d 6d 6i t d � d 6d 6i t d � d 6d 6i t d � d 6d 6i t d � d 6d  6|  _ i d! d" 6t d# � d 6i d$ d% 6d& 6i d' d" 6g d( 6d d d d d  g d) 6i d* d" 6t d+ � d 6i d* d% 6d& 6i d, d" 6g d( 6d d d d d  g d) 6i d- d" 6t d. � d 6i  d& 6d d d d d  g d) 6g |  _ d  S(/   NR�   R�   RF   R�   R�   R�   R�   i    R�   R�   s   createObject?type_name=ContactR�   s$   ++resource++bika.lims.images/add.pngR�   R�   i2   t   contactss4   /++resource++bika.lims.images/client_contact_big.pngt   ContactsR   s	   Full NameR�   t   getFullnameR�   s	   User Namet   Usernames   Email Addresst   getEmailAddresss   Business Phonet   getBusinessPhones   Mobile Phonet   getMobilePhoneR�   R�   R�   R�   R%   R�   R�   R�   R�   R&   R�   R�   R�   R�   (   R�   R'  R�   R�   RX   R�   R�   RW   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (   Rc   R<   R7   (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   %  sh    	
						




c         C   s6  t  j |  � } x t t | � � D]} | | j d � sA q" n  | | d } | j �  | | d <| j �  | | d <| j �  | | d <| j �  | | d <| j	 �  } | r� | p� d | | d <d | | d	 | | d f | | d
 d <| | d r" d | | d | | d f | | d
 d <q" q" W| S(   NRl   R*  R,  R-  R.  R   R+  s   <a href='%s'>%s</a>R�   R�   s   <a href='mailto:%s'>%s</a>(
   R   R�   R�   RV   R�   R*  R,  R-  R.  t   getUsername(   Rc   R,   R�   Rl   t   username(    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR�   b  s"     )0(   R|   R}   R   R   R   R�   R�   (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyR'  "  s   	=(<   t   AccessControlR    R   t   Products.Archetypes.configR   t   Products.CMFCore.utilsR   t&   Products.Five.browser.pagetemplatefileR   t	   bika.limsR   R   R   RW   t   bika.lims.browserR   t   bika.lims.browser.batchfolderR	   t!   bika.lims.browser.analysisrequestR
   R   t   bika.lims.browser.bika_listingR   t   bika.lims.browser.publishR   t   bika.lims.browser.sampleR   t   bika.lims.interfacesR   t   bika.lims.permissionst   bika.lims.subscribersR   R   t   bika.lims.utilsR   t   operatorR   t$   plone.app.content.browser.interfacesR   t#   plone.app.layout.globals.interfacesR   t	   zope.i18nR   t   zope.interfaceR   R9   R   R   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R  R'  (    (    (    s:   /home/campbell/repos/bika.lims/bika/lims/browser/client.pyt   <module>   sF   
�>DCBL!F>