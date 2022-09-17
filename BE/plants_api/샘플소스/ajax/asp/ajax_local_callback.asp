<%
Response.ContentType = "text/xml"
Response.AddHeader "Pragma", "no-cache"
Response.expires = -1
Response.buffer = True
Response.CharSet = "utf-8"

	
	url = "http://api.nongsaro.go.kr/service/" & request.Querystring

	Set httpObj = Server.CreateObject("WinHttp.WinHttpRequest.5.1")
	httpObj.open "GET", url, False
	
	httpObj.Send()
	httpObj.WaitForResponse
	
	If httpObj.Status = "200" Then
		getSiteSourceGet = httpObj.ResponseBody
		
		response.binaryWrite getSiteSourceGet
	Else
		getSiteSourceGet = null
	End If 
	
	Set httpObj = Nothing

%>