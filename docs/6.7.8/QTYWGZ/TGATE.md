<span class="anchor" id="f2b2c73a-12b2-490d-a957-7339325826b4"></span>
## 1.TGate简介
<p>TGate(CTP交易网关)是CTP fens组件的全新换代，相较于fens有着更轻量、客户端适配成本低、易维护、易使用等优点。用户可以通过查询的方式实时获取其所在中心可接入的服务地址信息，包括交易、行情、银期转账等服务地址，灵活设计策略选择地址。即使盘中切换了交易中心，客户端可自动快速获取新的地址接入。</p>
<span class="anchor" id="72648bc3-416c-45e7-8ad6-2bcec392ebac"></span>
## 2.TGate接入场景
<p>TGate连接CTP获取全量各中心前置地址列表以及用户与交易中心对应关系。配套提供的TGateAPi为终端实现统一接入管理提供完整的解决方案。用户终端通过TGateAPi连接TGate发起查询前置地址请求，无需登录，TGate根据客户请求返回所在交易中心全部可接入的服务地址。</p>
<p>无论客户是在CTP次中心，还是在异构分中心做交易，只需将其可连接的前置地址维护在CTP柜台，终端通过TGate获取地址列表，不必再做过滤即可接入所在中心的交易系统。即使盘中发生交易中心切换，对于终端也只需重新获取一次地址列表，重新连接即可，省略繁琐的站点切换。</p>
<span class="anchor" id="b4b60498-775e-4d42-a33b-c0301f099cd2"></span>
## 3.接口文件列表
<table>
<tr>
<td bgcolor="#0062A8"><font color="#FFFFFF" face="微软雅黑">文件名</font></td>
<td bgcolor="#0062A8"><font color="#FFFFFF" face="微软雅黑">详情</font></td>
</tr>
<tr>
<td><a href="..//TGateFtdcApi.h">TGateFtdcApi.h</a></td>
<td>交易接口C++头文件包含交易相关的指令。</td>
</tr>
<tr>
<td><a href="..//TGateFtdcApiStruct.h">TGateFtdcApiStruct.h</a></td>
<td>包含了所有用到的数据结构的头文件。</td>
</tr>
<tr>
<td><a href="..//TGateFtdcApiDataType.h">TGateFtdcApiDataType.h</a></td>
<td>包含了所有用到的数据类型的头文件。</td>
</tr>
<tr>
<td>tgateapi.dll</td>
<td rowspan="2">tgate的动态链接库和静态链接库。</td>
</tr>
<tr>
<td>tgateapi.lib</td>
</tr>
<tr>
<td>error.dtd</td>
<td rowspan="2">包含所有可能的错误信息。</td>
</tr>
<tr>
<td><a href="..//error_tgate.xml">error.xml</a></td>
</tr>
<tr>
<td>FTD_tgateapi.xml</td>
<td>FTD协议中用到的各种包和域</td>
</tr>
</table>
<span class="anchor" id="fc9e5199-5802-47a4-8452-c4cc5b193cf2"></span>
## 4.TGateApi使用介绍
<p>新增TGateAPI实现终端与交易网关的接入与通讯。</p>
<p>TGateAPI提供了两个接口，分别为CTGateFtdcApi和CTGateFtdcSpi。这两个接口对FTD协议进行了封装，方便客户端应用程序的开发。客户端应用程序可以通过CTGateFtdcApi发出操作请求，通过继承CTGateFtdcSpi并重载回调函数来处理后台服务的响应。与TradeApi的使用方法基本相同。</p>
<p>客户端调用网关API至少需要两个线程，一个是应用程序主线程，一个是网关API工作线程。应用程序与网关通讯是由 API工作线程驱动的。CTGateFtdcApi提供的接口是线程安全的，可以有多个应用程序线程同时发出请求。CTGateFtdcSpi提供的接口回调是由API工作线程驱动，通过实现SPI中的接口方法，可以从网关服务端收取所需数据。</p>
<p>如果重载的某个回调函数阻塞，则等于阻塞了API工作线程，API与网关的通讯会停止。因此，在CTGateFtdcSpi派生类的回调函数中，应迅速返回，此处不建议在回调中发送请求或处理其他代码逻辑，不要阻塞。</p>
<blockquote>
<p>注意以下事项：</p>
<p>最大支持5000个终端连接</p>
<p>在途查询流控为1笔</p>
<p><a href="../../HQJK/CTHOSTFTDCMDAPI/RELEASE/">Release</a>不是线程安全的，多线程使用需要加锁</p>
<p>API请求的输入参数不能为 NULL。 </p>
<p>API请求的返回参数，0表示正确，其他表示错误。</p>
</blockquote>
<span class="anchor" id="0d86b822-4da9-418d-9eaf-86324083ac4c"></span>
## 5.TGateApi示例
<p>本次API新增一个查询接口ReqQryTGIpAddrParam，入参BrokerID、UserID要求必填。</p>
<p>下面通过一个简单的代码示例，带大家快速了解下网关API的使用方法。该示例演示了API如何接入网关并查询服务地址的过程。</p>
<pre><code>1   #include "TGateFtdcApi.h"           
2   #include "TGateFtdcApiDataType.h"           
3   #include "TGateFtdcApiStruct.h"         
4   #include &lt;iostream&gt;         
5   #include &lt;string&gt;           
6   #include &lt;Windows.h&gt;            
7               
8   class TGUser : public CTGateFtdcSpi         
9   {           
10  public:         
11      TGUser(){};     
12      ~TGUser(){};        
13              
14      ///服务地址参数查询     
15      void ReqQryTGIpAddrParam()      
16      {       
17          string m_sTGFrontAddr = "tcp://127.0.0.1";  
18          string m_sBrokerid = "0001";    
19          string m_sUserid = "123456789"; 
20          ///创建TGateApi实例 
21          CTGateFtdcApi *m_pTGApi = CTGateFtdcApi::CreateTGateFtdcApi();  
22          m_pTGApi-&gt;RegisterSpi(this);    
23          m_pTGApi-&gt;RegisterTGAddr(const_cast&lt;char *&gt;(m_sTGFrontAddr.c_str()));   
24          ///调用TGateApi查询服务地址请求   
25          CTGateFtdcQryTGIpAddrParamField* pQryTGIpAddrParamField = new CTGateFtdcQryTGIpAddrParamField;  
26          memset(pQryTGIpAddrParamField, 0, sizeof(pQryTGIpAddrParamField));  
27          ///该查询接口的重要传参   
28          strcpy(pQryTGIpAddrParamField-&gt;BrokerID, m_sBrokerid.c_str());  
29          strcpy(pQryTGIpAddrParamField-&gt;UserID, m_sUserid.c_str());  
30          int RequestID = 0;  
31          int rst = m_pTGApi-&gt;ReqQryTGIpAddrParam(pQryTGIpAddrParamField, RequestID); 
32          Sleep(1000);    
33      }       
34              
35      ///服务地址参数查询响应       
36      void OnRspQryTGIpAddrParam(CTGateFtdcTGIpAddrParamField* pTGIpAddrParam, CTGateFtdcRspInfoField* pRspInfo, int nRequestID, bool bIsLast)            
37      {       
38          string m_sFrontAddr = pTGIpAddrParam-&gt;Address;  
39          printf("&lt;OnRspQryTGIpAddrParam&gt;\n");    
40      }       
41  }           
</code></pre>
<blockquote>
<p>注意：连到非tgate地址，会返回-4 "API验证失败"的报错</p>
</blockquote>
