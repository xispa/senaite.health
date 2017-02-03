from Products.ZCTextIndex.ParseTree import ParseError
from bika.lims.browser import BrowserView
from Products.CMFCore.utils import getToolByName
import plone
import json


class ajaxGetPatientInfo(BrowserView):
    """ Grab details of newly created patient (#420)
    """
    def __call__(self):
        plone.protect.CheckAuthenticator(self.request)
        Fullname = self.request.get('Fullname', '')
        PatientUID = self.request.get('PatientUID', '')
        ClientPatientID = self.request.get('ClientPatientID', '')
        PatientID = self.request.get('PatientID','')
        ret = {'PatientID': '',
               'PatientUID': '',
               'ClientPatientID': '',
               'ClientID': '',
               'ClientUID': '',
               'ClientTitle': '',
               'ClientSysID': '',
               'PatientFullname': '',
               'PatientBirthDate': '',
               'PatientGender':'dk',
               'PatientMenstrualStatus':''}

        proxies = None
        if PatientUID:
            try:
                bpc = getToolByName(
                    self.context, 'bikahealth_catalog_patient_listing')
                proxies = bpc(UID=PatientUID)
            except ParseError:
                pass
        elif PatientID:
            try:
                bpc = getToolByName(
                    self.context, 'bikahealth_catalog_patient_listing')
                proxies = bpc(id=PatientID)
            except ParseError:
                pass
        elif ClientPatientID:
            try:
                bpc = getToolByName(
                    self.context, 'bikahealth_catalog_patient_listing')
                proxies = bpc(getClientPatientID=ClientPatientID)
            except ParseError:
                pass
        elif Fullname:
            try:
                bpc = getToolByName(
                    self.context, 'bikahealth_catalog_patient_listing')
                proxies = bpc(Title=Fullname,
                              sort_on='created',
                              sort_order='reverse')
            except ParseError:
                pass

        if not proxies:
            return json.dumps(ret)

        patient = proxies[0]
        ret = {'PatientID': patient.getPatientID,
               'PatientUID': patient.UID,
               'ClientPatientID': patient.getClientPatientID,
               'ClientUID': patient.getPrimaryReferrerID,
               'ClientTitle': patient.getPrimaryReferrerTitle,
               'ClientSysID': patient.getPrimaryReferrerID,
               'PatientFullname': patient.Title,
               'PatientBirthDate': self.ulocalized_time(patient.getBirthDate),
               'PatientGender': patient.getGender,
               'PatientMenstrualStatus': patient.getMenstrualStatus}
        return json.dumps(ret)
