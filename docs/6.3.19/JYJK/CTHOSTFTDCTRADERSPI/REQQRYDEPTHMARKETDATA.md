<p>请求查询行情，只能查询当前快照，不能查询历史行情。</p>
<p>响应: OnRspQryDepthMarketData</p>
<span class="anchor" id="af50c247-52f2-45d8-a6bf-29b023573a91"></span>
## 1.函数原型
<p>virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;</p>
<span class="anchor" id="882bfe97-a546-4764-a8de-72a0a6e63625"></span>
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
<span class="anchor" id="9baf0fdf-e85e-4e70-af7d-6bddd39c9afd"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ae6c5f88-9276-462c-a5aa-d60ac0acbb34"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="570d9ae0-7f55-4fcc-8849-45d8a8265d6c"></span>
## 5.FAQ
<p>无</p>
