<p>请求查询转帐流水。</p>
<p>响应：<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRANSFERSERIAL/">OnRspQryTransferSerial</a></p>
<span class="anchor" id="6b24029e-b1eb-4bb1-8225-0ec32b8df570"></span>
## 1.函数原型
<p>virtual int ReqQryTransferSerial(CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID) = 0;</p>
<span class="anchor" id="82aac73a-ff19-4ae8-b0d4-2d7e0968c23d"></span>
## 2.参数
<p>pQryTransferSerial：请求查询转帐流水</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankIDType</td>
<td style="TEXT-ALIGN: left;">BankID</td>
<td style="TEXT-ALIGN: left;">银行代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="3c1842ed-2062-48b2-bd70-05e998004db2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6783a5b2-7a36-41c3-818c-6cb84b8fb592"></span>
## 4.调用示例
<pre><code>CThostFtdcQryTransferSerialField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.AccountID, "1000001"); 
strcpy_s(a.BankID, “1”);
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryTransferSerial(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="2ce4b8a1-4af0-4619-940f-dde1e9057007"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">我在柜台上做了手工出入金，通过这个接口查不到？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>ReqQryTransferSerial不能查柜台手工出入金，只能查询到期货发起期货转银行或者银行转期货的内容。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
