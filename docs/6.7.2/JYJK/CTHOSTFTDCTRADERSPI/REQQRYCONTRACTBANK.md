<p>请求查询签约银行</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCONTRACTBANK/">OnRspQryContractBank</a></p>
<span class="anchor" id="a7a08c96-0eee-44d9-80b2-f67d96c5b0a6"></span>
## 1.函数原型
<p>virtual int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) = 0;</p>
<span class="anchor" id="68cc8f7a-4da3-4574-8a0b-bba503bd1116"></span>
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
<span class="anchor" id="5c2811cd-3751-4296-9b34-407dba5c5ea3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="849a2e13-2b64-420a-a812-3368b87b0acb"></span>
## 4.调用示例
<pre><code>CThostFtdcQryContractBankField a = { 0 };
strcpy_s(a.BrokerID, "9999");
m_pUserApi-&gt;ReqQryContractBank(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="43b1ca01-6239-4f4a-a8c8-c872bdc8f0d7"></span>
## 5.FAQ
<p>无</p>
