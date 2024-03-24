<p>资金账户口令更新请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQTRADINGACCOUNTPASSWORDUPDATE/">ReqTradingAccountPasswordUpdate</a>后，该方法被调用。</p>
<span class="anchor" id="544c02d6-9e78-45c0-a8d9-db2ab93c1cba"></span>
## 1.函数原型
<p>virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d0df091f-37f1-48d7-b5c8-c4e047fd3b89"></span>
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
<span class="anchor" id="d0d4b1cc-8ef1-41d3-83a4-c7f185e3eb03"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b5034f19-3940-4b35-bf21-577031ca7a5a"></span>
## 4.FAQ
<p>无</p>
