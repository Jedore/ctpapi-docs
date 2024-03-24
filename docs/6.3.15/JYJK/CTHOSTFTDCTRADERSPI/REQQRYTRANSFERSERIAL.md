<p>请求查询转帐流水。</p>
<p>响应：OnRspQryTransferSerial</p>
<span class="anchor" id="ddcbb331-cbfe-41a1-8c77-7b8b550d5096"></span>
## 1.函数原型
<p>virtual int ReqQryTransferSerial(CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID) = 0;</p>
<span class="anchor" id="d4582a1f-33c3-428e-83e8-e2a35bc73620"></span>
## 2.参数
<p>pQryTransferSerial：请求查询转帐流水</p>
<pre><code>struct CThostFtdcQryTransferSerialField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///银行编码
    TThostFtdcBankIDType BankID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="4c2e9428-6bdb-46ec-8107-ac2abae09c15"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6e15a48b-1cc3-40c3-a184-5b673124b23c"></span>
## 4.调用示例
<pre><code>CThostFtdcQryTransferSerialField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.AccountID, "1000001"); 
strcpy_s(a.BankID, “1”);
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryTransferSerial(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="387b165f-0ff1-42f6-9067-8ca370554bde"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">我在柜台上做了手工出入金，通过这个接口查不到？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>ReqQryTransferSerial不能查柜台手工出入金，只能查询到期货发起期货转银行或者银行转期货的内容。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
