<p>查询用户当前支持的认证模式，暂不支持</p>
<p>响应: OnRspUserAuthMethod</p>
<span class="anchor" id="75042b2c-23ed-439b-a643-f9a7f828adbe"></span>
## 1.函数原型
<p>virtual int ReqUserAuthMethod(CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID) = 0;</p>
<span class="anchor" id="eda5dac1-c177-40b9-b9b9-2e5dd47301e9"></span>
## 2.参数
<p>pReqUserAuthMethod：用户发出获取安全安全登陆方法请求</p>
<pre><code>struct CThostFtdcReqUserAuthMethodField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d6762971-c35e-49ab-abd0-cb682d809d47"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="abe17411-2377-418f-9d0b-60ba37b992ec"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4127ae19-4bc3-4dc3-a393-449cb5c5e81c"></span>
## 5.FAQ
<p>无</p>
