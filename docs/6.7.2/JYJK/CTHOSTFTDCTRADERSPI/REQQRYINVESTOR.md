<p>请求查询投资者</p>
<p>响应：<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTOR/">OnRspQryInvestor</a></p>
<span class="anchor" id="782ff9af-1538-4c0e-b2ad-bd6c01811d29"></span>
## 1.函数原型
<p>virtual int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) = 0;</p>
<span class="anchor" id="15060994-d4fe-4ec3-802a-1d11127a47aa"></span>
## 2.参数
<p>pQryInvestor：查询投资者</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="ce8d8d40-d249-403d-a2bf-75278d8a53f0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8624b0c3-82a3-430b-bff9-47d5803b7b2b"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryInvestor(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="4888c2a7-b37a-464e-85aa-0ed4a5287872"></span>
## 5.FAQ
<p>无</p>
