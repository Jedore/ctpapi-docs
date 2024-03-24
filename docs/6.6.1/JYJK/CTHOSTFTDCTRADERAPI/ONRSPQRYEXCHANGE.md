<p>请求查询交易所响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGE/">ReqQryExchange</a>后，该方法被调用。</p>
<span class="anchor" id="bcb6791d-85e6-437d-8522-ecac4d76f3c0"></span>
## 1.函数原型
<p>virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="9955fa1b-c02e-495c-a347-3c56e23707d4"></span>
## 2.参数
<p>pExchange：交易所</p>
<pre><code>struct CThostFtdcExchangeField
{
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///交易所名称
    TThostFtdcExchangeNameType ExchangeName;
    ///交易所属性
    TThostFtdcExchangePropertyType ExchangeProperty;
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
<span class="anchor" id="e673a5b8-3d9b-40f5-861e-af7328cf1bb3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3caf8939-8595-421c-a1bc-e4d25131f7ea"></span>
## 4.FAQ
<p>无</p>
