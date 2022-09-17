<% @CODEPAGE="65001" language="VBScript" %>
<html>
<head>
<meta http-dquiv="Content-Type" content="text/html" charset="utf-8">
<title>사료 검색</title>
<script type='text/javascript'>
//상세보기
function fncDtl(cNo){
	with(document.searchApiForm){
		cntntsNo.value = cNo;
		method="get";
		action = "gardenDtl.asp";
		target = "_self";
		submit();
	}
}

//검색
function fncSearch(){
	with(document.searchApiForm){
		lightChkVal.value = fncCheckValue(document.getElementsByName("lightChk"));
		grwhstleChkVal.value = fncCheckValue(document.getElementsByName("grwhstleChk"));
		lefcolrChkVal.value = fncCheckValue(document.getElementsByName("lefcolrChk"));
		lefmrkChkVal.value = fncCheckValue(document.getElementsByName("lefmrkChk"));
		flclrChkVal.value = fncCheckValue(document.getElementsByName("flclrChk"));
		fmldecolrChkVal.value = fncCheckValue(document.getElementsByName("fmldecolrChk"));
		ignSeasonChkVal.value = fncCheckValue(document.getElementsByName("ignSeasonChk"));
		winterLwetChkVal.value = fncCheckValue(document.getElementsByName("winterLwetChk"));
		pageNo.value = "1";
		method="get";
		action = "gardenList.asp";
		target = "_self";
		submit();
	}
}
//페이지 이동
function fncGoPage(page){
	with(document.searchApiForm){
		pageNo.value = page;
		method="get";
		action = "gardenList.asp";
		target = "_self";
		submit();
	}
}

function fncWordTypeOption(){
	var wordType = document.getElementById("wordType")[document.getElementById("wordType").selectedIndex].value;

 	if(wordType == "cntntsSj"){
 		document.getElementById("englishSrch").style.display="none";
 		document.getElementById("koreanSrch").style.display="block";
	}else if(wordType == "plntbneNm"){
 		document.getElementById("koreanSrch").style.display="none";
 		document.getElementById("englishSrch").style.display="block";
	}
}

function fncContSearch(word){
	document.searchApiForm.word.value = word;
	fncSearch();
}

function fncCheckValue(obj){
	var checkValue = "";

	for(var i=0; i<obj.length; i++){
		if(obj[i].checked == true){
			checkValue += obj[i].value + ",";
		}
	}

	if(checkValue!="") checkValue = checkValue.substring(0, checkValue.length-1);

	return checkValue;
}
</script>
</head>
<body>
<h4><strong> * 샘플화면은 디자인을 적용하지 않았으니, 개별 사이트의 스타일에 맞게 코딩하시기 바랍니다.</strong></h4>
<h3><strong>실내정원용 식물</strong></h3>
<hr>

<%
sType = Request("sType")
wordType = Request("wordType")
word = Request("word")
priceType = Request("priceType")
priceTypeSel = Request("priceTypeSel")
waterCycleSel = Request("waterCycleSel")
%>

<form name="searchApiForm">
<input type="hidden" name="cntntsNo">
<input type="hidden" name="pageNo" value="<%=Request("pageNo")%>">
<input type="hidden" name="word" value="<%=Request("word")%>">
<input type="hidden" name="lightChkVal" value="<%=Request("lightChkVal")%>">
<input type="hidden" name="grwhstleChkVal" value="<%=Request("grwhstleChkVal")%>">
<input type="hidden" name="lefcolrChkVal" value="<%=Request("lefcolrChkVal")%>">
<input type="hidden" name="lefmrkChkVal" value="<%=Request("lefmrkChkVal")%>">
<input type="hidden" name="flclrChkVal" value="<%=Request("flclrChkVal")%>">
<input type="hidden" name="fmldecolrChkVal" value="<%=Request("fmldecolrChkVal")%>">
<input type="hidden" name="ignSeasonChkVal" value="<%=Request("ignSeasonChkVal")%>">
<input type="hidden" name="winterLwetChkVal" value="<%=Request("winterLwetChkVal")%>">
<table width="100%" border="1" cellSpacing="0" cellPadding="0">
	<colgroup>
		<col width="20%"/>
		<col width="80%"/>
	</colgroup>
	<tr>
		<th>
			<select name="sType">
				<option value="sCntntsSj" <% If sType="sCntntsSj" Then Response.Write("selected") Else Response.Write("") End If%>>식물명</option>
				<option value="sPlntbneNm" <% If sType="sPlntbneNm" Then Response.Write("selected") Else Response.Write("") End If%>>한명</option>
				<option value="sPlntzrNm" <% If sType="sPlntzrNm" Then Response.Write("selected") Else Response.Write("") End If%>>영명</option>
			</select>
		</th>
		<td>
			<input type="text" name="sText" value="<%=Request("sText")%>">
			<input type="button" name="search" value="검색" onclick="return fncSearch();"/>
		</td>
	</tr>
	<tr>
		<th>
			<select id="wordType" name="wordType" onchange="javascript:fncWordTypeOption(); return false;">
				<option value="cntntsSj" <% If wordType="cntntsSj" Then Response.Write("selected") Else Response.Write("") End If%>>국명</option>
				<option value="plntbneNm" <% If wordType="plntbneNm" Then Response.Write("selected") Else Response.Write("") End If%>>학명</option>
			</select>
		</th>
		<td>
			<div id="koreanSrch" style="display: <% If wordType="" Then Response.Write("block") Else If wordType="cntntsSj" Then Response.Write("block") Else Response.Write("none") End If End If%>;">
				<a href="#" onclick="javascript:fncContSearch('ㄱ');return false;" style="font-weight:<% If word="ㄱ" Then Response.Write("bold") Else Response.Write("") End If%>">ㄱ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄴ');return false;" style="font-weight:<% If word="ㄴ" Then Response.Write("bold") Else Response.Write("") End If%>">ㄴ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄷ');return false;" style="font-weight:<% If word="ㄷ" Then Response.Write("bold") Else Response.Write("") End If%>">ㄷ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄹ');return false;" style="font-weight:<% If word="ㄹ" Then Response.Write("bold") Else Response.Write("") End If%>">ㄹ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅁ');return false;" style="font-weight:<% If word="ㅁ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅁ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅂ');return false;" style="font-weight:<% If word="ㅂ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅂ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅅ');return false;" style="font-weight:<% If word="ㅅ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅅ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅇ');return false;" style="font-weight:<% If word="ㅇ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅇ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅈ');return false;" style="font-weight:<% If word="ㅈ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅈ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅊ');return false;" style="font-weight:<% If word="ㅊ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅊ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅋ');return false;" style="font-weight:<% If word="ㅋ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅋ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅌ');return false;" style="font-weight:<% If word="ㅌ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅌ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅍ');return false;" style="font-weight:<% If word="ㅍ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅍ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅎ');return false;" style="font-weight:<% If word="ㅎ" Then Response.Write("bold") Else Response.Write("") End If%>">ㅎ</a>
			</div>
			<div id="englishSrch" style="display: <% If wordType="plntbneNm" Then Response.Write("block") Else Response.Write("none") End If %>;">
				<a href="#" onclick="javascript:fncContSearch('A');return false;" style="font-weight:<% If word="A" Then Response.Write("bold") Else Response.Write("") End If%>;">A</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('B');return false;" style="font-weight:<% If word="B" Then Response.Write("bold") Else Response.Write("") End If%>;">B</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('C');return false;" style="font-weight:<% If word="C" Then Response.Write("bold") Else Response.Write("") End If%>;">C</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('D');return false;" style="font-weight:<% If word="D" Then Response.Write("bold") Else Response.Write("") End If%>;">D</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('E');return false;" style="font-weight:<% If word="E" Then Response.Write("bold") Else Response.Write("") End If%>;">E</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('F');return false;" style="font-weight:<% If word="F" Then Response.Write("bold") Else Response.Write("") End If%>;">F</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('G');return false;" style="font-weight:<% If word="G" Then Response.Write("bold") Else Response.Write("") End If%>;">G</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('H');return false;" style="font-weight:<% If word="H" Then Response.Write("bold") Else Response.Write("") End If%>;">H</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('I');return false;" style="font-weight:<% If word="I" Then Response.Write("bold") Else Response.Write("") End If%>;">I</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('J');return false;" style="font-weight:<% If word="J" Then Response.Write("bold") Else Response.Write("") End If%>;">J</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('K');return false;" style="font-weight:<% If word="K" Then Response.Write("bold") Else Response.Write("") End If%>;">K</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('L');return false;" style="font-weight:<% If word="L" Then Response.Write("bold") Else Response.Write("") End If%>;">L</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('M');return false;" style="font-weight:<% If word="M" Then Response.Write("bold") Else Response.Write("") End If%>;">M</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('N');return false;" style="font-weight:<% If word="N" Then Response.Write("bold") Else Response.Write("") End If%>;">N</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('O');return false;" style="font-weight:<% If word="O" Then Response.Write("bold") Else Response.Write("") End If%>;">O</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('P');return false;" style="font-weight:<% If word="P" Then Response.Write("bold") Else Response.Write("") End If%>;">P</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Q');return false;" style="font-weight:<% If word="Q" Then Response.Write("bold") Else Response.Write("") End If%>;">Q</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('R');return false;" style="font-weight:<% If word="R" Then Response.Write("bold") Else Response.Write("") End If%>;">R</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('S');return false;" style="font-weight:<% If word="S" Then Response.Write("bold") Else Response.Write("") End If%>;">S</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('T');return false;" style="font-weight:<% If word="T" Then Response.Write("bold") Else Response.Write("") End If%>;">T</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('U');return false;" style="font-weight:<% If word="U" Then Response.Write("bold") Else Response.Write("") End If%>;">U</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('V');return false;" style="font-weight:<% If word="V" Then Response.Write("bold") Else Response.Write("") End If%>;">V</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('W');return false;" style="font-weight:<% If word="W" Then Response.Write("bold") Else Response.Write("") End If%>;">W</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('X');return false;" style="font-weight:<% If word="X" Then Response.Write("bold") Else Response.Write("") End If%>;">X</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Y');return false;" style="font-weight:<% If word="Y" Then Response.Write("bold") Else Response.Write("") End If%>;">Y</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Z');return false;" style="font-weight:<% If word="Z" Then Response.Write("bold") Else Response.Write("") End If%>;">Z</a>
			</div>
		</td>
	</tr>
<%
	'apiKey - 농사로 Open API에서 신청 후 승인되면 확인가능
	apiKey = "인증키를입력하세요"
	'서비스 명
	serviceName = "garden"
	'오퍼레이션 명
	operationName = Array("lightList", "grwhstleList", "lefcolrList", "lefmrkList", "flclrList", "fmldecolrList", "ignSeasonList", "winterLwetList", "priceTypeList", "waterCycleList")

	Set xmlDOMS=Server.CreateObject("Scripting.Dictionary")

	For i=0 To UBound(operationName)
		'XML 받을 URL 생성
		parameter = "/" & serviceName & "/" & operationName(i)
		parameter = parameter & "?apiKey="&apiKey

		targetURL = "http://api.nongsaro.go.kr/service" & parameter

		'농사로 Open API 통신 시작
		Set xmlHttp = Server.CreateObject("Microsoft.XMLHTTP")
		xmlHttp.Open "GET", targetURL, False
		xmlHttp.Send

		Set oStream = CreateObject("ADODB.Stream")
		oStream.Open
		oStream.Position = 0
		oStream.Type = 1
		oStream.Write xmlHttp.ResponseBody
		oStream.Position = 0
		oStream.Type = 2
		oStream.Charset = "utf-8"
		sText = oStream.ReadText
		oStream.Close

		xmlDOMS.Add operationName(i), sText
	Next

	'검색조건
	For n=0 To UBound(operationName)

	'오퍼레이션명
	operNm = operationName(n)
	'검색조조건 명
	srchNm = ""
	'타입명
	typeNm = ""
	'타입명 값
	typeVal = ""

	'광도요구
	If operNm = "lightList" Then
		srchNm = "광도요구"
		typeNm = "lightChk"
		typeVal = "lightChkVal"
	'생육형태
	ElseIf operNm = "grwhstleList" Then
		srchNm = "생육형태"
		typeNm = "grwhstleChk"
		typeVal = "grwhstleChkVal"
	'잎색
	ElseIf operNm = "lefcolrList" Then
		srchNm = "잎색"
		typeNm = "lefcolrChk"
		typeVal = "lefcolrChkVal"
	'잎무늬
	ElseIf operNm = "lefmrkList" Then
		srchNm = "잎 무늬"
		typeNm = "lefmrkChk"
		typeVal = "lefmrkChkVal"
	'꽃 색
	ElseIf operNm = "flclrList" Then
		srchNm = "꽃 색"
		typeNm = "flclrChk"
		typeVal = "flclrChkVal"
	'열매 색
	ElseIf operNm = "fmldecolrList" Then
		srchNm = "열매 색"
		typeNm = "fmldecolrChk"
		typeVal = "fmldecolrChkVal"
	'꽃피는 계절
	ElseIf operNm = "ignSeasonList" Then
		srchNm = "꽃피는 계절"
		typeNm = "ignSeasonChk"
		typeVal = "ignSeasonChkVal"
	'겨울최저온도
	ElseIf operNm = "winterLwetList" Then
		srchNm = "겨울 최저온도"
		typeNm = "winterLwetChk"
		typeVal = "winterLwetChkVal"
	'가격대
	ElseIf operNm = "priceTypeList" Then
		srchNm = "가격대"
	'물주기
	ElseIf operNm = "waterCycleList" Then
		srchNm = "물주기"
	End if

	sText = xmlDOMS.Item(operNm)

	Set xmlDOM = server.CreateObject("MSXML.DOMDOCUMENT")
	xmlDOM.async = False
	xmlDOM.LoadXML sText
	'농사 Open API 통신 끝

	Set listItem = xmlDOM.SelectNodes("//items")
	cnt = listItem(0).childNodes.length
	Set items = listItem(0).childNodes

	Response.Write("<tr><th>"+srchNm+"</th><td>")
	If cnt = 0 Then
		Response.Write("조회한 정보가 없습니다.")
	Else
		For i=0 To cnt-1
			 Set itemNode = items.item(i)
			If NOT itemNode Is Nothing Then
				'코드
				If NOT itemNode.SelectSingleNode("code") is Nothing Then
					code = itemNode.SelectSingleNode("code").text
				End If
				'코드명
				If NOT itemNode.SelectSingleNode("codeNm") is Nothing Then
					codeNm = itemNode.SelectSingleNode("codeNm").text
				End If
			End If

			If operNm ="priceTypeList"  Then
			 If i=0 Then
%>
				<input type="radio" id="priceType" name="priceType" value="big" <% If priceType="big" Then Response.Write("checked") Else Response.Write("") End If %>/>대형&nbsp;
				<input type="radio" id="priceType" name="priceType" value="medium" <% If priceType="medium" Then Response.Write("checked") Else Response.Write("") End If %>/>중형&nbsp;
				<input type="radio" id="priceType" name="priceType" value="3" <% If priceType="3" Then Response.Write("checked") Else Response.Write("") End If %>/>소형&nbsp;
				<select id="priceTypeSel" name="priceTypeSel">
				<option value="">선택하세요.</option>
<%
			 End If
%>
			<option value="<%=code%>" <% If priceTypeSel=code Then Response.Write("selected") Else Response.Write("") End If %>><%=codeNm%></option>
<%
			ElseIf operNm ="waterCycleList" Then
				If i=0 Then
%>
				<select id="waterCycleSel" name="waterCycleSel">
				<option value="">선택하세요.</option>
<%
				End If
%>
			<option value="<%=code%>" <% If waterCycleSel=code Then Response.Write("selected") Else Response.Write("") End If %>><%=codeNm%></option>
<%
			Else
%>
				<input type="checkbox" id="<%=typeNm%>" name="<%=typeNm%>" value="<%=code%>" <%
				If Not Request(typeVal) is Nothing  Then
					chkVal = Request(typeVal)
					chkValArr = Split(chkVal, ",")
					For j=0 To UBound(chkValArr)
						If code = chkValArr(j) Then
							Response.Write("checked")
						End if
					Next
				End if%> ><%=codeNm%>&nbsp;
<%
			End if
		 Set itemNode = Nothing
		 Next
	End If
	If operNm ="priceTypeList" OR operNm ="waterCycleList" Then
		Response.Write("</select>")
	End If
	Response.Write("</td></tr>")
	Next

%>
		</table>
	</form>
<%
If true Then
	'오퍼레이션 명
	operationName = "gardenList"

	'XML 받을 URL 생성
	parameter = "/" & serviceName & "/" & operationName
	parameter = parameter & "?apiKey=" & apiKey
	parameter = parameter & "&pageNo=" & Request("pageNo")

	searchNmArr = Array("sType", "sText", "wordType", "word", "lightChkVal", "grwhstleChkVal", "lefcolrChkVal", "lefmrkChkVal", "flclrChkVal", "fmldecolrChkVal", "ignSeasonChkVal", "winterLwetChkVal", "priceType", "priceTypeSel", "waterCycleSel")
	For i=0 To UBound(searchNmArr)
		If Not Request(searchNmArr(i)) Is Nothing And Request(searchNmArr(i)) <> "" Then
			parameter = parameter & "&" & searchNmArr(i) & "=" & Server.URLEncode(Request(searchNmArr(i)))
		End If
	Next

	targetURL = "http://api.nongsaro.go.kr/service" & parameter

	'농사로 Open API 통신 시작
	Set xmlHttp = Server.CreateObject("Microsoft.XMLHTTP")
	xmlHttp.Open "GET", targetURL, False
	xmlHttp.Send

	Set oStream = CreateObject("ADODB.Stream")
	oStream.Open
	oStream.Position = 0
	oStream.Type = 1
	oStream.Write xmlHttp.ResponseBody
	oStream.Position = 0
	oStream.Type = 2
	oStream.Charset = "utf-8"
	sText = oStream.ReadText
	oStream.Close

	Set xmlDOM = server.CreateObject("MSXML.DOMDOCUMENT")
	xmlDOM.async = False
	xmlDOM.LoadXML sText
	'농사 Open API 통신 끝

	Set listItem = xmlDOM.SelectNodes("//items")
	cnt = listItem(0).childNodes.length
	Set items = listItem(0).childNodes

'페이징 처리를 위한 값 받기
	'한 페이지에 제공할 건수
	Set numOfRows = xmlDOM.SelectNodes("//numOfRows")
	If Not numOfRows(0) Is Nothing Then numOfRowsText= numOfRows(0).Text Else numOfRowsText = "10" End If
	'조회할 페이지 번호
	Set pageNo = xmlDOM.SelectNodes("//pageNo")
	If Not pageNo(0) Is Nothing Then pageNoText= pageNo(0).Text Else pageNoText = "1" End If
	'조회된 총 건수
	Set totalCount = xmlDOM.SelectNodes("//totalCount")
	If Not totalCount(0) Is Nothing Then totalCountText= totalCount(0).Text Else totalCountText = "" End If

	If cnt-3 = 0 Then
		Response.Write("<h3>조회한 정보가 없습니다.</h3>")
	Else
	%>
		<hr>
		<table width="100%" border="1" cellSpacing="0" cellPadding="0">
	<%
			For i=0 To cnt-4
			   Set itemNode = items.item(i)
				If NOT itemNode Is Nothing Then
					'컨텐츠번호
					If NOT itemNode.SelectSingleNode("cntntsNo") is Nothing Then
						cntntsNo = itemNode.SelectSingleNode("cntntsNo").text
					End If
					'컨텐츠 제목
					If NOT itemNode.SelectSingleNode("cntntsSj") is Nothing Then
						cntntsSj = itemNode.SelectSingleNode("cntntsSj").text
					End If
					'저장 파일명
					If NOT itemNode.SelectSingleNode("rtnStreFileNm") is Nothing Then
						rtnStreFileNm = itemNode.SelectSingleNode("rtnStreFileNm").text
					End If
					'파일 경로
					If NOT itemNode.SelectSingleNode("rtnFileCours") is Nothing Then
						rtnFileCours = itemNode.SelectSingleNode("rtnFileCours").text
					End If
					rtnStreFileNmArr=Split(rtnStreFileNm,"|")
					rtnFileCoursArr=Split(rtnFileCours,"|")
				End If

	%>
		<tr>
				<td width="15%"><img src="http://www.nongsaro.go.kr/<%=rtnFileCoursArr(0)%>/<%=rtnStreFileNmArr(0)%>" width="128" height="103"></img></td>
				<td width="85%">
				<a href="javascript:fncDtl('<%=cntntsNo%>');"><%=cntntsSj%></a>
				</td>
		</tr>
	<%
			   Set itemNode = Nothing
			Next
			Response.Write("</table>")
		End If

		'페이징 처리
		function ceil(x)
	        dim temp
	        temp = Round(x)
	        if temp < x then
	            temp = temp + 1
	        end if
	        ceil = temp
	    end function


		pageGroupSize = 10
		pageSize = Int(numOfRowsText)


		start = Int(pageNoText)

		currentPage = Int(pageNoText)

		startRow = (currentPage - 1) * pageSize + 1
		endRow = currentPage * pageSize
		count = Int(totalCountText)
		number=0

		number=count-(currentPage-1)*pageSize

		pageGroupCount = count/(pageSize*pageGroupSize)

		numPageGroup = Int(ceil(currentPage/pageGroupSize))

		If count > 0 Then
			pageCount = Int(count / pageSize)


			If (count Mod pageSize) = 0 Then
				pageCount = pageCount + 0
			Else
				pageCount = pageCount + 1
			End If

			startPage = pageGroupSize*(numPageGroup-1)+1
			endPage = startPage + pageGroupSize-1
			prtPageNo = 0

			If endPage > pageCount Then
				endPage = pageCount
			End If

			If numPageGroup > 1 Then
				prtPageNo = (numPageGroup-2)*pageGroupSize+1
				Response.Write("<a href='javascript:fncGoPage("&prtPageNo&");'>[이전]</a>")
			End If

			i=startPage
			While i<=endPage

				prtPageNo = i
				Response.Write("<a href='javascript:fncGoPage("&prtPageNo&");'>")

				If currentPage = i Then
					Response.Write("<strong>["&i&"]</strong>")
				Else
					Response.Write("["&i&"]")
				End If

				Response.Write("</a>")

				i = i+1
			Wend

			If numPageGroup < pageGroupCount Then
				prtPageNo = (numPageGroup*pageGroupSize+1)
				Response.Write("<a href='javascript:fncGoPage("&prtPageNo&");'>[다음]</a>")
			End If
		End If
		'페이징처리 끝
End If
%>
</body>
</html>
