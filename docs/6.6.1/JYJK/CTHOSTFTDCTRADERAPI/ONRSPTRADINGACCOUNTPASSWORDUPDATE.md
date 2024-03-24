<p>资金账户口令更新请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQTRADINGACCOUNTPASSWORDUPDATE/">ReqTradingAccountPasswordUpdate</a>后，该方法被调用。</p>
<span class="anchor" id="7a99f2a0-ebcd-488e-816a-bdd85fc329f8"></span>
## 1.函数原型
<p>virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c2113acb-afdc-4a17-bc80-76fe6d373e23"></span>
## 2.参数
<p>pTradingAccountPasswordUpdate：资金账户口令变更域</p>
<pre><code>struct CThostFtdcTradingAccountPasswordUpdateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///原来的口令
    TThostFtdcPasswordType OldPassword;
    ///新的口令
    TThostFtdcPasswordType NewPassword;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="997ec750-b64b-49d8-a691-2d202f5688ac"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d6bb2ef3-ec17-45fb-9aa3-6e1832ce23b5"></span>
## 4.FAQ
<p>无</p>
