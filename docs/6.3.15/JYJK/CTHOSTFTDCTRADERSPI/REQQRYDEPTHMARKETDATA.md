<p>请求查询行情，只能查询当前快照，不能查询历史行情。</p>
<p>响应: OnRspQryDepthMarketData</p>
<span class="anchor" id="f3eee479-854c-40d7-9cd1-351445da8027"></span>
## 1.函数原型
<p>virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;</p>
<span class="anchor" id="882cb30f-c459-459e-832d-6ad5e6d061fd"></span>
## 2.参数
<p>pQryDepthMarketData：查询行情</p>
<pre><code>struct CThostFtdcQryDepthMarketDataField
{
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="3b2d2166-6aca-46f1-9375-b9c6b8c1150c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="50acf949-021c-4ecc-9906-65d994101c97"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a07472d4-79fc-43ca-a3b4-9d2a87b5d855"></span>
## 5.FAQ
<p>无</p>
