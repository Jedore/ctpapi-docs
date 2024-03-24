<p>请求查询签约银行</p>
<p>响应: OnRspQryContractBank</p>
<span class="anchor" id="1eda1972-f46d-4b00-b372-3d841c15632b"></span>
## 1.函数原型
<p>virtual int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) = 0;</p>
<span class="anchor" id="d95cadba-6e35-4239-b27e-1d3f2e5c35f3"></span>
## 2.参数
<p>pQryContractBank：查询签约银行请求</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankIDType</td>
<td style="TEXT-ALIGN: left;">BankID</td>
<td style="TEXT-ALIGN: left;">银行代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankBrchIDType</td>
<td style="TEXT-ALIGN: left;">BankBrchID</td>
<td style="TEXT-ALIGN: left;">银行分中心代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="3640fc7f-a82b-4666-b7e4-94a1541804c8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="688b259a-95a3-45ae-b84b-59d1bd457018"></span>
## 4.调用示例
<pre><code>CThostFtdcQryContractBankField a = { 0 };
strcpy_s(a.BrokerID, "9999");
m_pUserApi-&gt;ReqQryContractBank(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="21ddb8ab-c646-44ec-b53d-887878baf67b"></span>
## 5.FAQ
<p>无</p>
