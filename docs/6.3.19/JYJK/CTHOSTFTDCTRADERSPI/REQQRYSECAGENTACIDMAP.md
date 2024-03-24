<p>请求查询二级代理操作员银期权限</p>
<p>响应: OnRspQrySecAgentACIDMap</p>
<span class="anchor" id="74e98b55-4215-4ae4-af7d-ca238f6fb598"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentACIDMap(CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) = 0;</p>
<span class="anchor" id="c65c62d3-d0cb-492a-b1c0-a91e70db6e43"></span>
## 2.参数
<p>pQrySecAgentACIDMap：二级代理操作员银期权限查询</p>
<pre><code>struct CThostFtdcQrySecAgentACIDMapField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///资金账户
    TThostFtdcAccountIDType AccountID;
    ///币种
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="9f8031ab-4ec5-4416-af72-0482dc51ad5e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f4397669-5a08-4016-983f-5bc8d3532f10"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8da73ab8-0c2d-4aba-ac2d-b8a410cf402e"></span>
## 5.FAQ
<p>无</p>
