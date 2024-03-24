<p>请求查询交易所响应，当执行ReqQryExchange后，该方法被调用。</p>
<span class="anchor" id="f4f95d45-9328-4199-b163-60d42d165e98"></span>
## 1.函数原型
<p>virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c4bf57b5-d925-4d22-8197-eb137d1a05f4"></span>
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
<span class="anchor" id="fb8b798e-1b08-48ff-8e4a-83890ee0ed6c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="206d155a-232d-419f-a3f6-fa4e28f4344d"></span>
## 4.FAQ
<p>无</p>
