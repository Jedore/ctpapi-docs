<p>资金账户口令更新请求响应，当执行ReqTradingAccountPasswordUpdate后，该方法被调用。</p>
<span class="anchor" id="dd3c5543-f55e-4a82-8e90-e60d73c7dc4a"></span>
## 1.函数原型
<p>virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="36ac4f2d-e365-4b69-8941-071afab868b8"></span>
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
<span class="anchor" id="0b894955-4256-445b-853a-6d1eb83ce826"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4901533d-7d1b-4076-9097-19c6b4610f8f"></span>
## 4.FAQ
<p>无</p>
