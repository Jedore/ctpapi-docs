<p>请求查询交易所响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGE/">ReqQryExchange</a>后，该方法被调用。</p>
<span class="anchor" id="b7f87412-71c0-43b4-8121-b54bcab97402"></span>
## 1.函数原型
<p>virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1a63e9a1-8a18-4466-af07-44089fd5679e"></span>
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
<span class="anchor" id="fb8a6778-4ed2-4957-9082-0d44c88d9aaa"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9ede8246-c7e6-4c16-93de-60fa8fbe2cb5"></span>
## 4.FAQ
<p>无</p>
