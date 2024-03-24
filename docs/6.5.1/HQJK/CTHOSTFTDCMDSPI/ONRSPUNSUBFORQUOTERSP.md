<p>取消订阅询价应答，当UnSubscribeForQuoteRsp后，调用此接口。</p>
<span class="anchor" id="16417f85-f52e-41c6-9b23-1f94bddbda7b"></span>
## 1.函数原型
<p>virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b640517f-cb0f-46a9-a129-7185046ef9ad"></span>
## 2.参数
<p>pSpecificInstrument：指定的合约</p>
<pre><code>struct CThostFtdcSpecificInstrumentField
{
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="31cbe97a-7ee0-4f07-b7df-a533bfe009b4"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="71e8c9b9-8adf-4161-89e2-5bf1cb54776b"></span>
## 4.FAQ
<p>无</p>
