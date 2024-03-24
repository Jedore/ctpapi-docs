<p>请求查询签约银行</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCONTRACTBANK/">OnRspQryContractBank</a></p>
<span class="anchor" id="1f467226-701b-4d40-9b21-f4c659c300be"></span>
## 1.函数原型
<p>virtual int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) = 0;</p>
<span class="anchor" id="7d942527-de67-4640-9900-dea1e06bc854"></span>
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
<span class="anchor" id="de7abfb0-8401-46b4-a62b-3f5bc1bd84c0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3bf7853e-5a98-4215-824c-beb49bf76b12"></span>
## 4.调用示例
<pre><code>CThostFtdcQryContractBankField a = { 0 };
strcpy_s(a.BrokerID, "9999");
m_pUserApi-&gt;ReqQryContractBank(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="094737ae-1b84-4a85-9b79-2a11b0ecf993"></span>
## 5.FAQ
<p>无</p>
