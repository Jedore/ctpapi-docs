<p>请求查询银期签约关系</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYACCOUNTREGISTER/">OnRspQryAccountregister</a></p>
<span class="anchor" id="c5d11ef7-f818-4d0d-a3e3-f783601d2d14"></span>
## 1.函数原型
<p>virtual int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) = 0;</p>
<span class="anchor" id="7cdf11a1-6757-41a5-86c9-9426c3c40998"></span>
## 2.参数
<p>pQryAccountregister：请求查询银期签约关系</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankIDType</td>
<td style="TEXT-ALIGN: left;">BankID</td>
<td style="TEXT-ALIGN: left;">银行代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankBrchIDType</td>
<td style="TEXT-ALIGN: left;">BankBranchID</td>
<td style="TEXT-ALIGN: left;">银行分支机构代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>字段值填写正确时，均无查询结果</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="c8230dc0-4c2c-4b39-b9ea-dde83bdf5363"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="16420c59-6fb1-493a-b8bb-9f59ec940939"></span>
## 4.调用示例
<pre><code>CThostFtdcQryAccountregisterField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.AccountID, "1000001");
strcpy_s(a.BankID, "1");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryAccountregister(&amp;a, 1);
</code></pre>
<span class="anchor" id="de996a1f-4789-4ecb-b9d7-47a90cfdc968"></span>
## 5.FAQ
<p>无</p>
