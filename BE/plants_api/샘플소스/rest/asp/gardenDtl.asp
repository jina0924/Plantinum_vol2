<% @CODEPAGE="65001" language="VBScript" %>
<html>
<head>
<meta http-dquiv="Content-Type" content="text/html" charset="utf-8">
<title>RDA 인테러뱅</title>
</head>
<body>
<h4><strong> * 샘플화면은 디자인을 적용하지 않았으니, 개별 사이트의 스타일에 맞게 코딩하시기 바랍니다.</strong></h4>
<h3><strong>RDA 인테러뱅</strong></h3>
<hr>

<%
	'apiKey - 농사로 Open API에서 신청 후 승인되면 확인가능
	apiKey = "인증키를입력하세요"
	'서비스 명
	serviceName = "garden"
	'오퍼레이션 명
	operationName = "gardenDtl"

	'XML 받을 URL 생성
	parameter = "/" & serviceName & "/" & operationName
	parameter = parameter & "?apiKey="&apiKey
	parameter = parameter & "&cntntsNo=" & Request("cntntsNo")

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

	Set item = xmlDOM.SelectNodes("//body")
	cnt = item(0).childNodes.length

	If cnt = 0 Then
		Response.Write("<h3>조회한 정보가 없습니다.</h3>")
	Else
		'컨텐츠 번호
		Set cntntsNo = xmlDOM.SelectNodes("//cntntsNo")
		If Not cntntsNo(0) Is Nothing Then cntntsNoText= cntntsNo(0).Text Else cntntsNoText = "" End If
		'식물학명
		Set plntbneNm = xmlDOM.SelectNodes("//plntbneNm")
		If Not plntbneNm(0) Is Nothing Then plntbneNmText= plntbneNm(0).Text Else plntbneNmText = "" End If
		'식물 영명
		Set plntzrNm = xmlDOM.SelectNodes("//plntzrNm")
		If Not plntzrNm(0) Is Nothing Then plntzrNmText= plntzrNm(0).Text Else plntzrNmText = "" End If
		'유통 명
		Set distbNm = xmlDOM.SelectNodes("//distbNm")
		If Not distbNm(0) Is Nothing Then distbNmText= distbNm(0).Text Else distbNmText = "" End If
		'과 명
		Set fmlNm = xmlDOM.SelectNodes("//fmlNm")
		If Not fmlNm(0) Is Nothing Then fmlNmText= fmlNm(0).Text Else fmlNmText = "" End If
		'원산지명
		Set orgplceInfo = xmlDOM.SelectNodes("//orgplceInfo")
		If Not orgplceInfo(0) Is Nothing Then orgplceInfoText= orgplceInfo(0).Text Else orgplceInfoText = "" End If
		'조언정보
		Set adviseInfo = xmlDOM.SelectNodes("//adviseInfo")
		If Not adviseInfo(0) Is Nothing Then adviseInfoText= adviseInfo(0).Text Else adviseInfoText = "" End If
		'이미지 평가 링크 명
		Set imageEvlLinkCours = xmlDOM.SelectNodes("//imageEvlLinkCours")
		If Not imageEvlLinkCours(0) Is Nothing Then imageEvlLinkCoursText= imageEvlLinkCours(0).Text Else imageEvlLinkCoursText = "" End If
		'성장 높이 정보
		Set growthHgInfo = xmlDOM.SelectNodes("//growthHgInfo")
		If Not growthHgInfo(0) Is Nothing Then growthHgInfoText= growthHgInfo(0).Text Else growthHgInfoText = "" End If
		'성장 넓이 정보
		Set growthAraInfo = xmlDOM.SelectNodes("//growthAraInfo")
		If Not growthAraInfo(0) Is Nothing Then growthAraInfoText= growthAraInfo(0).Text Else growthAraInfoText = "" End If
		'잎형태 정보
		Set lefStleInfo = xmlDOM.SelectNodes("//lefStleInfo")
		If Not lefStleInfo(0) Is Nothing Then lefStleInfoText= lefStleInfo(0).Text Else lefStleInfoText = "" End If
		'냄새 코드
		Set smellCode = xmlDOM.SelectNodes("//smellCode")
		If Not smellCode(0) Is Nothing Then smellCodeText= smellCode(0).Text Else smellCodeText = "" End If
		'독성 정보
		Set toxctyInfo = xmlDOM.SelectNodes("//toxctyInfo")
		If Not toxctyInfo(0) Is Nothing Then toxctyInfoText= toxctyInfo(0).Text Else toxctyInfoText = "" End If
		'번식 시기
		Set prpgtEraInfo = xmlDOM.SelectNodes("//prpgtEraInfo")
		If Not prpgtEraInfo(0) Is Nothing Then prpgtEraInfoText= prpgtEraInfo(0).Text Else prpgtEraInfoText = "" End If
		'기타시기 정보
		Set etcEraInfo = xmlDOM.SelectNodes("//etcEraInfo")
		If Not etcEraInfo(0) Is Nothing Then etcEraInfoText= etcEraInfo(0).Text Else etcEraInfoText = "" End If
		'관리수준 코드
		Set managelevelCode = xmlDOM.SelectNodes("//managelevelCode")
		If Not managelevelCode(0) Is Nothing Then managelevelCodeText= managelevelCode(0).Text Else managelevelCodeText = "" End If
		'성장속도 코드
		Set grwtveCode = xmlDOM.SelectNodes("//grwtveCode")
		If Not grwtveCode(0) Is Nothing Then grwtveCodeText= grwtveCode(0).Text Else grwtveCodeText = "" End If
		'생육 온도 코드
		Set grwhTpCode = xmlDOM.SelectNodes("//grwhTpCode")
		If Not grwhTpCode(0) Is Nothing Then grwhTpCodeText= grwhTpCode(0).Text Else grwhTpCodeText = "" End If
		'겨울최저 온도 코드
		Set winterLwetTpCode = xmlDOM.SelectNodes("//winterLwetTpCode")
		If Not winterLwetTpCode(0) Is Nothing Then winterLwetTpCodeText= winterLwetTpCode(0).Text Else winterLwetTpCodeText = "" End If
		'습도 코드
		Set hdCode = xmlDOM.SelectNodes("//hdCode")
		If Not hdCode(0) Is Nothing Then hdCodeText= hdCode(0).Text Else hdCodeText = "" End If
		'비트 정보
		Set frtlzrInfo = xmlDOM.SelectNodes("//frtlzrInfo")
		If Not frtlzrInfo(0) Is Nothing Then frtlzrInfoText= frtlzrInfo(0).Text Else frtlzrInfoText = "" End If
		'토양 정보
		Set soilInfo = xmlDOM.SelectNodes("//soilInfo")
		If Not soilInfo(0) Is Nothing Then soilInfoText= soilInfo(0).Text Else soilInfoText = "" End If
		'물주기 봄 코드
		Set watercycleSprngCode = xmlDOM.SelectNodes("//watercycleSprngCode")
		If Not watercycleSprngCode(0) Is Nothing Then watercycleSprngCodeText= watercycleSprngCode(0).Text Else watercycleSprngCodeText = "" End If
		'물주기 여름 코드
		Set watercycleSummerCode = xmlDOM.SelectNodes("//watercycleSummerCode")
		If Not watercycleSummerCode(0) Is Nothing Then watercycleSummerCodeText= watercycleSummerCode(0).Text Else watercycleSummerCodeText = "" End If
		'물주기 가을 코드
		Set watercycleAutumnCode = xmlDOM.SelectNodes("//watercycleAutumnCode")
		If Not watercycleAutumnCode(0) Is Nothing Then watercycleAutumnCodeText= watercycleAutumnCode(0).Text Else watercycleAutumnCodeText = "" End If
		'물주기 겨울 코드
		Set watercycleWinterCode = xmlDOM.SelectNodes("//watercycleWinterCode")
		If Not watercycleWinterCode(0) Is Nothing Then watercycleWinterCodeText= watercycleWinterCode(0).Text Else watercycleWinterCodeText = "" End If
		'병충해 관리 정보
		Set dlthtsManageInfo = xmlDOM.SelectNodes("//dlthtsManageInfo")
		If Not dlthtsManageInfo(0) Is Nothing Then dlthtsManageInfoText= dlthtsManageInfo(0).Text Else dlthtsManageInfoText = "" End If
		'특별관리 정보
		Set speclmanageInfo = xmlDOM.SelectNodes("//speclmanageInfo")
		If Not speclmanageInfo(0) Is Nothing Then speclmanageInfoText= speclmanageInfo(0).Text Else speclmanageInfoText = "" End If
		'기능성 정보
		Set fncltyInfo = xmlDOM.SelectNodes("//fncltyInfo")
		If Not fncltyInfo(0) Is Nothing Then fncltyInfoText= fncltyInfo(0).Text Else fncltyInfoText = "" End If
		'화분직경 대 정보
		Set flpodmtBigInfo = xmlDOM.SelectNodes("//flpodmtBigInfo")
		If Not flpodmtBigInfo(0) Is Nothing Then flpodmtBigInfoText= flpodmtBigInfo(0).Text Else flpodmtBigInfoText = "" End If
		'화분직경 대 정보
		Set flpodmtMddlInfo = xmlDOM.SelectNodes("//flpodmtMddlInfo")
		If Not flpodmtMddlInfo(0) Is Nothing Then flpodmtMddlInfoText= flpodmtMddlInfo(0).Text Else flpodmtMddlInfoText = "" End If
		'화분직여 소 정보
		Set flpodmtSmallInfo = xmlDOM.SelectNodes("//flpodmtSmallInfo")
		If Not flpodmtSmallInfo(0) Is Nothing Then flpodmtSmallInfoText= flpodmtSmallInfo(0).Text Else flpodmtSmallInfoText = "" End If
		'가로 대 정보
		Set widthBigInfo = xmlDOM.SelectNodes("//widthBigInfo")
		If Not widthBigInfo(0) Is Nothing Then widthBigInfoText= widthBigInfo(0).Text Else widthBigInfoText = "" End If
		'가로 중 정보
		Set widthMddlInfo = xmlDOM.SelectNodes("//widthMddlInfo")
		If Not widthMddlInfo(0) Is Nothing Then widthMddlInfoText= widthMddlInfo(0).Text Else widthMddlInfoText = "" End If
		'가로 소 정보
		Set widthSmallInfo = xmlDOM.SelectNodes("//widthSmallInfo")
		If Not widthSmallInfo(0) Is Nothing Then widthSmallInfoText= widthSmallInfo(0).Text Else widthSmallInfoText = "" End If
		'세로 대 정보
		Set vrticlBigInfo = xmlDOM.SelectNodes("//vrticlBigInfo")
		If Not vrticlBigInfo(0) Is Nothing Then vrticlBigInfoText= vrticlBigInfo(0).Text Else vrticlBigInfoText = "" End If
		'세로 중 정보
		Set vrticlMddlInfo = xmlDOM.SelectNodes("//vrticlMddlInfo")
		If Not vrticlMddlInfo(0) Is Nothing Then vrticlMddlInfoText= vrticlMddlInfo(0).Text Else vrticlMddlInfoText = "" End If
		'세로 소 정보
		Set vrticlSmallInfo = xmlDOM.SelectNodes("//vrticlSmallInfo")
		If Not vrticlSmallInfo(0) Is Nothing Then vrticlSmallInfoText= vrticlSmallInfo(0).Text Else vrticlSmallInfoText = "" End If
		'높이 대 정보
		Set hgBigInfo = xmlDOM.SelectNodes("//hgBigInfo")
		If Not hgBigInfo(0) Is Nothing Then hgBigInfoText= hgBigInfo(0).Text Else hgBigInfoText = "" End If
		'높이 중 정보
		Set hgMddlInfo = xmlDOM.SelectNodes("//hgMddlInfo")
		If Not hgMddlInfo(0) Is Nothing Then hgMddlInfoText= hgMddlInfo(0).Text Else hgMddlInfoText = "" End If
		'높이 소 정보
		Set hgSmallInfo = xmlDOM.SelectNodes("//hgSmallInfo")
		If Not hgSmallInfo(0) Is Nothing Then hgSmallInfoText= hgSmallInfo(0).Text Else hgSmallInfoText = "" End If
		'볼륨 대 정보
		Set volmeBigInfo = xmlDOM.SelectNodes("//volmeBigInfo")
		If Not volmeBigInfo(0) Is Nothing Then volmeBigInfoText= volmeBigInfo(0).Text Else volmeBigInfoText = "" End If
		'볼륨 중 정보
		Set volmeMddlInfo = xmlDOM.SelectNodes("//volmeMddlInfo")
		If Not volmeMddlInfo(0) Is Nothing Then volmeMddlInfoText= volmeMddlInfo(0).Text Else volmeMddlInfoText = "" End If
		'볼륨 소 정보
		Set volmeSmallInfo = xmlDOM.SelectNodes("//volmeSmallInfo")
		If Not volmeSmallInfo(0) Is Nothing Then volmeSmallInfoText= volmeSmallInfo(0).Text Else volmeSmallInfoText = "" End If
		'가격 대 정보
		Set pcBigInfo = xmlDOM.SelectNodes("//pcBigInfo")
		If Not pcBigInfo(0) Is Nothing Then pcBigInfoText= pcBigInfo(0).Text Else pcBigInfoText = "" End If
		'가격 중 정보
		Set pcMddlInfo = xmlDOM.SelectNodes("//pcMddlInfo")
		If Not pcMddlInfo(0) Is Nothing Then pcMddlInfoText= pcMddlInfo(0).Text Else pcMddlInfoText = "" End If
		'가격 소 정보
		Set pcSmallInfo = xmlDOM.SelectNodes("//pcSmallInfo")
		If Not pcSmallInfo(0) Is Nothing Then pcSmallInfoText= pcSmallInfo(0).Text Else pcSmallInfoText = "" End If
		'관리요구도 코드
		Set managedemanddoCode = xmlDOM.SelectNodes("//managedemanddoCode")
		If Not managedemanddoCode(0) Is Nothing Then managedemanddoCodeText= managedemanddoCode(0).Text Else managedemanddoCodeText = "" End If

%>
<table  border="1" cellspacing="0" cellpadding="0">
		<colgroup>
			<col width="15%">
			<col width="*">
		</colgroup>
		<tr>
            <th>식물학명</th>
            <td><%=plntbneNmText%></td>
        </tr>
        <tr>
            <th>식물영명</th>
            <td><%=plntzrNmText%></td>
        </tr>
        <tr>
            <th>유통명</th>
            <td><%=distbNmText%></td>
        </tr>
        <tr>
            <th>과명</th>
            <td><%=fmlNmText%></td>
        </tr>
        <tr>
            <th>원산지 정보</th>
            <td><%=orgplceInfoText%></td>
        </tr>
        <tr>
            <th>조언 정보</th>
            <td><%=adviseInfoText%></td>
        </tr>
        <tr>
            <th>이미지 평가 링크 경로</th>
            <td><%=imageEvlLinkCoursText%></td>
        </tr>
        <tr>
            <th>성장 높이 정보</th>
            <td><%=growthHgInfoText%></td>
        </tr>
        <tr>
            <th>성장 넓이 정보</th>
            <td><%=growthAraInfoText%></td>
        </tr>
        <tr>
            <th>잎 형태 정보</th>
            <td><%=lefStleInfoText%></td>
        </tr>
        <tr>
            <th>냄새 코드</th>
            <td><%=smellCodeText%></td>
        </tr>
        <tr>
            <th>독성 정보</th>
            <td><%=toxctyInfoText%></td>
        </tr>
        <tr>
            <th>번식 시기 정보</th>
            <td><%=prpgtEraInfoText%></td>
        </tr>
        <tr>
            <th>기타 시기 정보</th>
            <td><%=etcEraInfoText%></td>
        </tr>
        <tr>
            <th>관리수준 코드</th>
            <td><%=managelevelCodeText%></td>
        </tr>
        <tr>
            <th>생장속도 코드</th>
            <td><%=grwtveCodeText%></td>
        </tr>
        <tr>
            <th>생육 온도 코드</th>
            <td><%=grwhTpCodeText%></td>
        </tr>
        <tr>
            <th>겨울 최저 온도 코드</th>
            <td><%=winterLwetTpCodeText%></td>
        </tr>
        <tr>
            <th>습도 코드</th>
            <td><%=hdCodeText%></td>
        </tr>
        <tr>
            <th>비료 정보</th>
            <td><%=frtlzrInfoText%></td>
        </tr>
        <tr>
            <th>토양 정보</th>
            <td><%=soilInfoText%></td>
        </tr>
        <tr>
            <th>물주기 봄 코드</th>
            <td><%=watercycleSprngCodeText%></td>
        </tr>
        <tr>
            <th>물주기 여름 코드</th>
            <td><%=watercycleSummerCodeText%></td>
        </tr>
        <tr>
            <th>물주기 가을 코드</th>
            <td><%=watercycleAutumnCodeText%></td>
        </tr>
        <tr>
            <th>물주기 겨울 코드</th>
            <td><%=watercycleWinterCodeText%></td>
        </tr>
        <tr>
            <th>병충해 관리 정보</th>
            <td><%=dlthtsManageInfoText%></td>
        </tr>
        <tr>
            <th>특별관리 정보</th>
            <td><%=speclmanageInfoText%></td>
        </tr>
        <tr>
            <th>기능성 정보</th>
            <td><%=fncltyInfoText%></td>
        </tr>
        <tr>
            <th>화분직경 대 정보</th>
            <td><%=flpodmtBigInfoText%></td>
        </tr>
        <tr>
            <th>화분직경 중 정보</th>
            <td><%=flpodmtMddlInfoText%></td>
        </tr>
        <tr>
            <th>화분직경 소 정보</th>
            <td><%=flpodmtSmallInfoText%></td>
        </tr>
        <tr>
            <th>가로 대 정보</th>
            <td><%=widthBigInfoText%></td>
        </tr>
        <tr>
            <th>가로 중 정보</th>
            <td><%=widthMddlInfoText%></td>
        </tr>
        <tr>
            <th>가로 소 정보</th>
            <td><%=widthSmallInfoText%></td>
        </tr>
        <tr>
            <th>세로 대 정보</th>
            <td><%=vrticlBigInfoText%></td>
        </tr>
        <tr>
            <th>세로 중 정보</th>
            <td><%=vrticlMddlInfoText%></td>
        </tr>
        <tr>
            <th>세로 소 정보</th>
            <td><%=vrticlSmallInfoText%></td>
        </tr>
        <tr>
            <th>높이 대 정보</th>
            <td><%=hgBigInfoText%></td>
        </tr>
        <tr>
            <th>높이 중 정보</th>
            <td><%=hgMddlInfoText%></td>
        </tr>
        <tr>
            <th>높이 소 정보</th>
            <td><%=hgSmallInfoText%></td>
        </tr>
        <tr>
            <th>볼륨 대 정보</th>
            <td><%=volmeBigInfoText%></td>
        </tr>
        <tr>
            <th>볼륨 중 정보</th>
            <td><%=volmeMddlInfoText%></td>
        </tr>
        <tr>
            <th>볼륨 소 정보</th>
            <td><%=volmeSmallInfoText%></td>
        </tr>
        <tr>
            <th>가격 대 정보</th>
            <td><%=pcBigInfoText%></td>
        </tr>
        <tr>
            <th>가격 중 정보</th>
            <td><%=pcMddlInfoText%></td>
        </tr>
        <tr>
            <th>가격 소 정보</th>
            <td><%=pcSmallInfoText%></td>
        </tr>
        <tr>
            <th>관리요구도 코드</th>
            <td><%=managedemanddoCodeText%></td>
        </tr>
	</table>
<%
	End If
%>
<input type="button" onclick="javascript:fncList();" value="목록"/>
<form name="searchApiForm">
<%
	searchNmArr = Array("pageNo","sType", "sText", "wordType", "word", "lightChkVal", "grwhstleChkVal", "lefcolrChkVal", "lefmrkChkVal", "flclrChkVal", "fmldecolrChkVal", "ignSeasonChkVal", "winterLwetChkVal", "priceType", "priceTypeSel", "waterCycleSel")
	For i=0 To UBound(searchNmArr)
	Response.Write("<input type='hidden' name='"&searchNmArr(i)&"' value='"&Request(searchNmArr(i))&"' />")
	Next
%>
</from>
<script type="text/javascript">
//목록이동
function fncList(){
	with(document.searchApiForm){
		method="get";
		action = "gardenList.asp";
		target = "_self";
		submit();
	}
}
</script>
</body>
</html>
