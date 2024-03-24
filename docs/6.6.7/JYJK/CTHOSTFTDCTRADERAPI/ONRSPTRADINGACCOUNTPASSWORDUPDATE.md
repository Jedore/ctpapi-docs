<p>资金账户口令更新请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQTRADINGACCOUNTPASSWORDUPDATE/">ReqTradingAccountPasswordUpdate</a>后，该方法被调用。</p>
<span class="anchor" id="2de47435-0e0c-494c-85ea-8b82eb6d508a"></span>
## 1.函数原型
<p>virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0356b610-6e39-4926-89cd-d1c4656b21b7"></span>
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
<span class="anchor" id="ff94cf26-c515-4705-a9ea-34f0308c1500"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="95c08626-e34b-4905-8053-1753f5921a68"></span>
## 4.FAQ
<p>无</p>
