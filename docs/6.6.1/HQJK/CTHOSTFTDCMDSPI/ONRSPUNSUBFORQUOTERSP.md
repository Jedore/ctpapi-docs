<p>取消订阅询价应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEFORQUOTERSP/">UnSubscribeForQuoteRsp</a>后，调用此接口。</p>
<span class="anchor" id="d3098ca3-0312-48ec-8f7b-1165d772edf8"></span>
## 1.函数原型
<p>virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a3724d3a-0369-4f7d-968b-930f788af801"></span>
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
<span class="anchor" id="08e287c9-f83b-4d49-85dc-488f7090bc46"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="39d4ae44-f135-4ded-9a87-203e3b727c53"></span>
## 4.FAQ
<p>无</p>
